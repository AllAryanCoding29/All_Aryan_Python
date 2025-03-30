#Simple; should just check if ATM Pin is valid or not.
print("Hello, and welcome to My ATM Pin Validator. This does not collect your data or tells you what your ATM pin should be.")
def check():
    while True:
        atm = int(input("What ATM pin do you want to check? "))
        if len(f"{atm}") < 4:
            print("An ATM pin has to have at least 4 digits!")
        elif len(f"{atm}") < 6:
            print("Better, but you should have 6 digits to be safe.")
            restart = input("Type c to continue, and press enter to try again.")
            if restart == "c":
                print("Good ATM Pin.")
                restart = input("Doy you want to go again? (yes/no) ")
                if restart == "yes":
                    continue
                else:
                    print("Thanks for using My Atm Validator.")
                    break
            else:
                print("Good choice!")
        else:
            print("Good ATM Pin.")
            restart = input("Doy you want to go again? (yes/no) ")
            if restart == "yes":
                continue
            else:
                print("Thanks for using My Atm Validator.")
                break
check()