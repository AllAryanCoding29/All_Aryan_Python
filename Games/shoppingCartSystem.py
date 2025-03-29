print("Hello, and welcome to My Shopping Cart System! It is very similar to My Shopping Cart, with the improvement of multiple item capability and a receipt!")
shoppingList = []
itemCost=[]
itemQuantity = []
def new_cart_item():
    new = input("Please enter your next item: ")
    shoppingList.append(new)
    cost = float(input(f"How much is each {new}? "))
    itemCost.append(cost)
    quantity = int(input(f"How many {new}s are you buying? "))
    itemQuantity.append(quantity)
while True:
    newItem = input("Do you want to enter a new Item? (yes/no): ")
    if newItem != "yes" and newItem != "no":
        print("Invalid response. Enter yes or no, and case matters.")
    elif newItem == "yes":
        new_cart_item()
    else:
        break
def receipt():
    print("Here is your receipt:")
    total = []
    for i in range(0,len(shoppingList)):
        print(f"You bought {itemQuantity[i]} {shoppingList[i]}s for {itemQuantity[i] * itemCost[i]} dollars.")
        total.append(itemQuantity[i] * itemCost[i])
    print(f"Your total is {sum(total)} dollars.")
receipt()
print("Thank you for using My Shopping Cart System.")