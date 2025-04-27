from random import randrange

def dice_roll():
    return randrange(1, 7)

def guess():
    while True:
        number = input("Enter a guess from 1 to 6: ")
        possible = ["1", "2", "3", "4", "5", "6"]
        if number not in possible:
            print("You can only enter a number from 1 to 6.")
        else:
            return int(number)

def game():
    dice = dice_roll()
    player_guess = guess()
    if player_guess == dice:
        print(f"You guessed it! {dice} was the number!")
    else:
        print(f"The dice rolled {dice}, but you guessed {player_guess}. Try again to win!")

def restart():
    while True:
        player_restart = input("Press enter to play again and any other key to exit: ")
        if player_restart != "":
            print("Thanks for playing My Dice Guesser!")
            break
        else:
            print("Ok! You can play again!")
            game()

print("Welcome to My Dice Guesser!")
game()
restart()