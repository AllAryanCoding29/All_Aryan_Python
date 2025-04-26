todo = []
def todolist():
    while True:
        userinput = input("Type view, add, delete, or done to continue. ")
        if userinput != "view" and userinput != "add" and userinput != "delete" and userinput != "done":
            print("Incorrect Entry. Case Matters!")
        elif userinput == "view":
            print(todo)
        elif userinput == "add":
            todoItem = input("What do you want to add? ")
            todo.append(todoItem)
        elif userinput == "delete":
            confirmation = input("Type exactly what you want to remove (Case matters): ")
            if confirmation not in todo:
                print("Non-valid entry. Case Matters. See below for possible items.")
                print(todo)
            else:
                todo.remove(confirmation)
                print(f"Here is the list now: {todo}. You removed {confirmation} from todo.")
        else:
            print("Thanks for using My ToDo List!")
            break
print("Hello, and welcome to My ToDo list.")
todolist()