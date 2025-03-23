while True:
    value = int(input("What number from 1 - 100 would you like me to show:"))
    if 1 <= value <= 100:
        print(f"\nHere is the multiplication table of {value} up to 10:")
        for i in range(1, 11):
            print(f"{value} * {i} = {value * i}")
        restart = input("Press 1 to continue, Any other key to stop:")
        if restart != "1":
            print("Thanks for using My Multiplication Table!")
            break
    else:
        print("Bro, you gave the wrong input. Try again.")



