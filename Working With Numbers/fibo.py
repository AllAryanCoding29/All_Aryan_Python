restart = 0
while (restart < 2):
    num = input("How many sequence numbers do you want? 1 is the minimum. Please enter an Integer.\n")
    i=1
    pv=0
    ctrl=0
    v=1
    print("\nHere are the fibonacci values in order:")
    print(v)
    while (i < int(num)):
        print(v+pv)
        ctrl = v
        v = v + pv
        pv = ctrl
        i = i + 1;
    print("\nThank you for using My Fibonacci Calculator.")
    restart = input("Type 1 to restart, and 2 to exit the program!\n")
    match int(restart):
        case int(1):
            restart = 1
        case int(2):
            restart = 2
            print("See you later! Thanks Again!")
        case _: 
            print("Look's like you must have not entered the right number.\n")
            restart = input("Type 1 to restart, and 2 to exit the program!\n")
            match int(restart):
                case int(1):
                    restart = 1
                case int(2):
                    restart = 2
                    print("See you later! Thanks Again!")
                case _: 
                    print("Look's like you must have not entered the right number again. We will default to restarting!")
                    restart = 1