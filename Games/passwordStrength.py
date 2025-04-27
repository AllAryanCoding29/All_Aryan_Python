# Should have 8 characters
# Should have lowercase and uppercase letters
# Should include a number
print("Hello, welcome to My Password Strength Checker. Enter your own password below to test it out, or just to have fun!")
def check_password_contain_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def check():
    while True:
        password = input("Enter your password: ")
        if len(password) < 8:
            print("Not strong enough, try again. Tip: Make your password at least 8 characters.")
            print("You have 8 characters, but you are missing a number. Try again.")
        elif not any(char.isupper() for char in password):
            print("Add an Uppercase letter. Try again.")
        elif not any(char.islower() for char in password):
            print("Add a lowercase letter. Try again.")
        else:
            print(f"{password} is a great password. It has 8 characters, Upper and lowercase letters, and a number! Thanks for using My Password Strength Checker!")
            break
check()