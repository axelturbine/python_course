def play():
    import random

    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    while True:
        computer = random.choice(choices)
        player = input("Choose rock, paper or scissors: ").lower()
        
        if player == "quit":
            break

        print("Computer chose:", computer)

        if player not in choices:
            print("Invalid choice! Try again.")
        elif player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win!")
            player_score += 1
        elif player == "paper" and computer == "rock":
            print("You win!")
            player_score += 1
        elif player == "scissors" and computer == "paper":
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

    print("Final score - You:", player_score, "computer:", computer_score)

    if player_score > computer_score:
        print("You won the game!")
    elif computer_score > player_score:
        print("Computer won the game!")
    else:
        print("Its a draw")