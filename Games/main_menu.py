import Hangman as hangman
import Rock_Paper_Scissor as rps
import Car_Game_v2 as car_game

while True:
    print("\n🎮 Welcome to Axel's Game Collection!")
    print("-------------------------------")
    print("1. 🎯 Hangman")
    print("2. 🪨 Rock Paper Scissors")
    print("3. 🚗 Car Game")
    print("4. 🚪 Quit")

    choice = input("\nChoose a game: ")

    if choice == "1":
        hangman.play()
    elif choice == "2":
        rps.play()
    elif choice == "3":
        car_game.play()
    elif choice == "4":
        print("Thanks for playing! 👋")
        break
    else:
        print("Invalid choice! Pick 1, 2, 3 or 4.")