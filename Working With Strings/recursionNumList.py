num_list = []
reversed_list = []

def user_list():
    newNum = input("What number do you want to add? ")
    if newNum.isdigit():
        num_list.append(newNum)
        print(f"Ok! Here is the current list: {num_list}!")
        addNew = input("Press enter to reverse your line, and any other key to add more numbers! ")
        if addNew == "":
            print("Reversing...")
        else:
            print("Ok!")
            user_list()
    else:
        print("That is not a number. Try again!")
        user_list()

def list_reverser():
    user_list()
    reversed_list.append(num_list[::-1]) #do without using this
    print("Reversed!")
    print(f"Here is the original list: {num_list} \nHere is the reversed list: {reversed_list}")

def program_run():
    list_reverser()
    user_restart = input("Press enter to try again, and any other key to exit! ")
    if user_restart == "":
        print("Ok! Restarting...")
        num_list.clear()
        reversed_list.clear()
        program_run()
    else:
        print("Thanks for playing!")

print("Welcome to My Number list Reverser!")
program_run()