def read_list():
    items = set()
    with open("shopping_list.txt", "r") as file:
        for line in file:
            word = line
            items.add(word)
        return items

items = read_list()
list_of_items = []
for item in items:
    list_of_items.append(item)

def new_list(list_of_products):
    with open("new_shopping_list.txt", "w") as file:
        for i in range(len(list_of_products)):
            product = list_of_products[i]
            file.write(product + "\n")
    print("Process Completed!")

new_list(list_of_items)