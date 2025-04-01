print("Hello, and welcome to my Temperature Converter. Please enter a number below, and this program will convert it to Fahrenheit or Celsius!")
def number_check():
    while True:
        number = input("Please enter your original temperature: ")
        if number.isdigit():
            print("Okay!")
            break
        else:
            print("Enter a whole number only. Try again!")
    return float(number)
def convert_check():
    while True:
        conversion = input("What do you want to convert to? Enter c or f: ")
        if conversion != "c" and conversion != "f":
            print("Enter c or f only. C for Celsius, F for Fahrenheit. Case matters c/f!")
        else:
            print("Ok!")
            break
    return conversion
def convert():
    number = number_check()
    conversion = convert_check()
    if conversion == "f":
        print("Fun Fact: To convert from Celsius to Fahrenheit there is a simple equation! (C + 32) * 1.8 = Fahrenheit Degree, where C is the Celsius Degree.")
        f = (number + 32) * 1.8
        print(f"{number} degrees Celsius is the same as {f} degrees Fahrenheit.")
    else:
        print("Fun Fact! When turning Fahrenheit into Celsius, there is a simple equation that people can use! (F - 32)/1.8 = Celsius degree, where F is the Fahrenheit Degree.")
        c = (number - 32)/1.8
        print(f"{number} degrees Fahrenheit is the same as {c} degrees Celsius.")
def restart():
    while True:
        restart_input = input("Do you want to go again? (y/n): ")
        if restart_input != "y" and restart_input != "n":
            print("You can only enter y or n for yes and no respectively.")
        elif restart_input == "y":
            convert()
        else:
            print("Thanks for using my Temperature Converter.")
            break
convert()
restart()






