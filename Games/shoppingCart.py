while True:
    item = input("What are you buying? ")
    itemCost = float(input(f"How much is each {item}? "))
    itemQuantity = int(input(f"How many {item}s are you buying? "))
    print(f"Your total cost is {itemCost * itemQuantity} dollars for {itemQuantity} {item}s!")
    restart = input("Press 1 to restart, and Any other key to exit: ")
    if restart == "1":
        continue
    else:
        print("Thanks for using My Shopping Cart!")
        break
