def factorial():
    length = int(input("What factorial do you want?"))
    return length

number2 = factorial()
fact2 = 1

def recursive(fact, number):
    fact = fact * number
    number = number - 1
    if number != 1:
        print(f"Number so far: {fact}")
        recursive(fact, number)
    else:
        print(f"The final number is {fact}")

recursive(fact2, number2)