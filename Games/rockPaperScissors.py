from random import randrange
print("Hello, and welcome to My Rock, Paper, and Scissors Game!")
print("Play against the computer and have a tournament!")
print("If you don't want a tie, then you should enter an odd number of games just in case.")
number = int(input("How many games would you like to have? Enter a positive number: "))
while True:
    playerPoints = 0
    computerPoints = 0
    for i in range(0, number):
        print(f"Round {i + 1}:")
        computer = randrange(1, 4)
        if computer == 1:
            computer = "Rock"
        elif computer == 2:
            computer = "Scissors"
        else:
            computer = "Paper"
        while True:
            player = input("Type Rock, Paper, or Scissors (case matters): ")
            if player != "Rock" and player != "Paper" and player != "Scissors":
                print("Incorrect, Non-valid Entry. Case as prompted. Try again.")
            else:
                break
        if computer == player:
            print(f"The computer also played {computer}. It is a draw, so 1 point to both of you!")
            playerPoints = playerPoints + 1
            computerPoints = computerPoints + 1
        elif computer == "Rock" and player == "Scissors" or computer == "Scissors" and player == "Paper":
            print(f"The computer played {computer}, so you lose this point.")
            computerPoints = computerPoints + 1
        else:
            print(f"The computer played {computer}; You won the round! 1 point to you")
            playerPoints = playerPoints + 1
        print(f"You now have {playerPoints} points, and the computer now has {computerPoints} points.")
    if playerPoints > computerPoints:
        print(f"You won with {playerPoints} points. The computer had {computerPoints} points.")
        restart = int(input("Do you want to play again? If so, type the number of games you want. Else, enter 0: "))
        if restart > 0:
            number = restart
            print("Restarting...")
        else:
            print("Thanks for playing My Rock, Paper, and Scissors Game!")
            break
    elif computerPoints > playerPoints:
        print(f"It was close, but you unfortunately lost. The computer scored {computerPoints} points, and you scored {playerPoints} points.")
        restart = int(input("Do you want to play again? If so, type the number of games you want. Else, enter 0: "))
        if restart > 0:
            number = restart
            print("Restarting...")
        else:
            print("Thanks for playing My Rock, Paper, and Scissors Game!")
            break
    else:
        print("You got a tie! Play again to see if you can win!")
        restart = int(input("Do you want to play again? If so, type the number of games you want. Else, enter 0: "))
        if restart > 0:
            number = restart
            print("Restarting...")
        else:
            print("Thanks for playing My Rock, Paper, and Scissors Game!")
            break