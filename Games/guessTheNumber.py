from random import randrange
print("Hello, welcome to My Guessing Game!")
print("Enter different numbers from 1 - 100 until you get it right!")
print("Every time you guess, it will tell you if you are too low, or too high!")
print("Have Fun!")
def generate():
    return randrange(1,10)
num = generate()
while True:
    guess = int(input("Enter your guess:"))
    if guess < num:
        print("Too low, Try again!")
    elif guess > num:
        print("Too high, Try again!")
    elif guess == num:
        print("Great job, you guessed it!")
        restart = input("Type 1 to go again, and Any other key to leave:")
        if restart == "1":
            print("Restarting...")
            num = generate()
        else:
            print("Thanks for playing My Guessing Game!")
            break


