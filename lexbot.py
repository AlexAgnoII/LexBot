import discord
import asyncio
import random
from discord.ext.commands import Bot

from Features.Calculator.Calculator import Calculator
from Features.GamePicker.GamePicker import GamePicker

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



#Functions for features
async def ratingFeature(word, message):
    container = word.split()
    container[0] = ""
    sentence = " ".join(container)
    rating = random.randint(0, 101)
    await client.send_message(message.channel, sentence + " seems to be: **" +str(rating) + "/100** ")

@client.event
async def on_message(message):
    #print(message.author.nick +"(" + str(message.timestamp) + ")" + ": " + message.content)
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, "Fcuk you sim")
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('!rate'):
        await ratingFeature(message.content, message)

    elif message.content.startswith('!think'):
        counter = 0
        dots = None
        theDots = "Thinking."
        for i in range(0, 6):
            await asyncio.sleep(1)
            if counter == 0:
                dots = await client.send_message(message.channel, "Thinking.")
                counter += 1
            elif i != 5:
                theDots = theDots + "."
                await client.edit_message(dots, theDots)
            else:
                await client.edit_message(dots, "I think therefore I am!")
    elif message.content.startswith("!ASDASDASDASDASDASDASDASD"):
        while True:
            print("Enter what to say: ", end="")
            msg = input()
            if msg != "STOP!":
                await client.send_message(message.channel, msg)
            else:
                break
    elif message.content.startswith("!love"):
        await client.send_message(message.channel, "Landi mo pakyu")

    elif message.content.startswith("!whatdoweplay"):
        gp = GamePicker
        game = gp.chooseGame()
        await client.send_message(message.channel, game)

    elif message.content.startswith("!sendbobsandvegana"):
        await client.send_message(message.channel, "Do milk")

    elif message.content.startswith("!Hi"):
        if str(message.author) == ".exe#2004":
            await client.send_message(message.channel, "TANGINA MO " + message.author.nick + "!")
        else:
            await client.send_message(message.channel, "Hi " + message.author.nick + "!")
    elif message.content.startswith("!game"):
        await client.send_message(message.channel, "```Working on it```")

    elif message.content.startswith("!calc"):
        cal = Calculator(message.content)
        

        
#@client.event
#async def on_typing(channel, user, when):
        #await client.send_message(channel, "Hi " + user.nick + "!")


@client.event
async def on_message_delete(message):

    if str(message.author) != str(client.user):
        await client.send_message(message.channel, message.content + " was deleted!")
    else:
        print("Deleted Message > " + message.author.nick + ": " + message.content) 
        
                    
                

            





client.run('MzY0NjE4MjA1NDA4MjY0MTky.DLUh0A.Ta_Tw4ii9xcfOHbxvMfpBqQyQ88')
