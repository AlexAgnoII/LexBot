import random

class GamePicker:
    def __init__():
        print("GamePicker was called!")

    
    
    def chooseGame():
        choice = random.randint(1,6)
        game = None
        if choice == 1:
            game = "Dota 2"
        elif choice == 2:
            game = "CS:GO"
        elif choice == 3:
            game = "PUBG"
        elif choice == 4:
            game = "Overwatch"
        elif choice == 5:
            game = "Fortnite"
        else:
            game = "Do milk"
        return game
