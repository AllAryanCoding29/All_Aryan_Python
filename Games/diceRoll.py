from random import randint
print("Hello, welcome to My Dice Game. Roll the dice, and try to get a higher number than your friends.")
def roll():
        input("Hello player, press enter to roll the dice!")
        rolled = randint(1, 6)
        print(f"You rolled {rolled}")
        return rolled
def restart:
    cont = input("Would you like to go again? (yes/no).")
    if cont == "yes":
        return True
    else:
        print("Thanks for playing!")
        return False
def winner():
    if player1 > player2:
        print("Player 1 wins!")
    elif player1 == player2:
        print("Draw!")
    else:
        print("Player 2 wins!")
while True:
    print("Player 1, you're turn!")
    player1 = roll()
    print("Player 2, you're turn!")
    player2 = roll()
    winner()
    tf = restart()
    if tf:
        continue
    else:
        break
