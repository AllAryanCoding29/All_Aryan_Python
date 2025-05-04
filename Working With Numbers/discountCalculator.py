def user_input():
    item = input("What are you buying? ")
    price = float(input("How much is it? "))
    discount = float(input("What is the discount? "))
    return item, price, discount

def calculate(product, cost, percent_off):
    return round(cost * ((100 - percent_off)/100), ROUND_DIGITS)

def program_run():
    while True:
        product, cost, percent_off = user_input()
        after_discount = calculate(product, cost, percent_off)
        print(f"The {product} you are buying, after having a {percent_off} sale, costs {after_discount} dollars.")
        restart = input("If you want to go again, press enter, else press any other key to exit! ")
        if restart == "":
            program_run()
        else:
            print("Thanks for playing!")
            break

ROUND_DIGITS = 2
print("Welcome to My Discount Calculator!")
program_run()
