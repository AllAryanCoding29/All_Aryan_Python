# This is my calculator app
# This is the loop in which the calculator resets!
num = 0
while int(num) != 5 :
# This is the input receiver, and it can collect 2 strings and print them.
    val1, val2 = input("Enter 2 Integer Values(separated by ;): \n").split(";")
    print("First Value : " + val1)
    print("Second Value : " + val2)
# Quite lengthy description of what number does what on the calculator using the 2 values inputted above.
    num = input("Value For Operation (1 is for add, 2 is for sub, 3 is for mul, 4 is for div, 5 to exit) : \n")
# This is a switch - in python a match-case which I used to substitute if-else for the different cases/operations. I also had to use int to turn 
# strings into usable integers for my equations to work. Side Note : I need to catch exceptions for decimals entered in as I do not have float entered in.
    match int(num):
        case 1:
            result = int(val1) + int(val2)
            print(result)
        case 2:
            result = int(val1) - int(val2)
            print(result)
        case 3: 
            result = int(val1) * int(val2)
            print(result)
        case 4:
            result = int(val1) / int(val2)
            print(result)
        case 5:
            print("Thanks for Using My Calculator! See you Soon!")
        case _:
            print("Nice try! Try entering 1 - 5!")