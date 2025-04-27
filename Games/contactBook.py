contact = {}
def add():
    name = input("What do you want to call this contact? ")
    number = input("What is this contact's number? ")
    contact[name] = number
    print(f"Here is the current contact list: {contact}")

def delete():
    name = input("Who's contact do you want to Delete? ")
    if name not in contact:
        print("That name isn't in your contacts. Case matters.")
        print(contact)
    else:
        del contact[name]
        print(f"You deleted {name} from your contacts.")
        print(f"Here is your current list: {contact}")

def list_all():
    print(f"Here are all of your contacts: {contact}")

def lookup():
    name = input("Who's contact do you want to look up? ")
    if name not in contact:
        print("That name isn't in your contacts. Case matters.")
        print(contact)
    else:
        print(f"Here is {name}'s contact: {contact[name]}")

def done():
    confirm = input("Type enter to exit, and any other key to continue! ")
    if confirm != "":
        print("continuing...")
        return True
    else:
        print("Thanks for using My Contact Book!")
        return False

def run():
    while True:
        action = input("What do you want to do? You can add, search, delete, or view your contacts. To exit, type done. ")
        if action == "add":
            add()
        elif action == "search":
            lookup()
        elif action == "delete":
            delete()
        elif action == "view":
            list_all()
        elif action == "done":
            b = done()
            if b:
                continue
            else:
                break
        else:
            print("Invalid action. You can only type add, search, delete, view, or done.")

run()