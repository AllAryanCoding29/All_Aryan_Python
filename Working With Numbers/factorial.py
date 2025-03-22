# Here is my simple factorial calculator app.
# This is the restart loop so that users don't have to run the code over and over.
restart = 0
while (restart < 2):
# Here is the input, where I used int to take a number input.
    num = int(input("What number would you like factorialed?\n"))
# Here is the factorial loop I used to calculate the factorial.
    fact = 1
    while (num > 1):
        fact = fact * num
        num = num - 1
# Here I printed the factorial by printing fact, the changing value/variable in my loop.
    print("Here is the factorial value: ")
    print(fact)
# I used a switch here, which is actually match-case in python, to assign numbers to actions according to user input and catch exceptions.
    tryagain = 1
    while (tryagain != 1):
        restart = int(input("Please enter 1 to restart, or 2 to exit the program!\n"))
        match restart:
            case 1:
                print("Restarting...")
                tryagain = 0
            case 2:
                print("Exiting...")
                tryagain = 0
            case _:
                print("Sorry, you must've not entered 1 or 2. Try again")
                tryagain = 1
print("Thanks for using My Factorial Calculator!")