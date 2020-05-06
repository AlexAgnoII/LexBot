package org.AlexAgnoII.dmusic;

import com.sedmelluq.discord.lavaplayer.player.AudioPlayer;
import com.sedmelluq.discord.lavaplayer.player.AudioPlayerManager;
import com.sedmelluq.discord.lavaplayer.player.DefaultAudioPlayerManager;
import com.sedmelluq.discord.lavaplayer.source.AudioSourceManagers;
import com.sedmelluq.discord.lavaplayer.track.playback.NonAllocatingAudioFrameBuffer;
import discord4j.core.DiscordClient;
import discord4j.core.DiscordClientBuilder;
import discord4j.core.event.domain.message.MessageCreateEvent;
import discord4j.core.object.VoiceState;
import discord4j.core.object.entity.Member;
import discord4j.voice.AudioProvider;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

import java.util.HashMap;
import java.util.Map;

public class DMusic {

    private static final Map<String, Command> commands = new HashMap<>();

    static {
        commands.put("ping", event -> event.getMessage().getChannel()
                .flatMap(channel -> channel.createMessage("Pong!"))
                .then());

    }

    public DMusic(String token) {
        final AudioPlayerManager playerManager = new DefaultAudioPlayerManager();
        playerManager.getConfiguration().setFrameBufferFactory(NonAllocatingAudioFrameBuffer::new);
        AudioSourceManagers.registerRemoteSources(playerManager);

        final AudioPlayer player = playerManager.createPlayer();
        AudioProvider provider = new LavaPlayerAudioProvider(player);

        commands.put("join", event -> Mono.justOrEmpty(event.getMember())
                .flatMap(Member::getVoiceState)
                .flatMap(VoiceState::getChannel)
                .flatMap(channel->channel.join(spec->spec.setProvider(provider)))
                .then());


        final DiscordClientBuilder builder = DiscordClientBuilder.create(token);
        final DiscordClient client = builder.build();

        client.getEventDispatcher().on(MessageCreateEvent.class)
                .flatMap(event-> Mono.justOrEmpty(event.getMessage().getContent())
                        .flatMap(content -> Flux.fromIterable(commands.entrySet())
                                .filter(entry -> content.startsWith('!' + entry.getKey()))
                                .flatMap(entry -> entry.getValue().execute(event))
                                .next()))
                .subscribe();

        client.login().block();
    }

    public static void main(String[] args) {
        new DMusic(args[0]);
    }
}
