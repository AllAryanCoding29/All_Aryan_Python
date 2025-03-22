amount = int(input("Please enter the amount of values you wish to use: "))
array = []
for a in range(amount):
    num = int(input("Please enter each amount you wish in the array one by one : "))
    array.append(num)
# If print(a), it starts from 0 and goes to amount - 1.
print(array)
print("Thanks for using My Array Printer progam.")