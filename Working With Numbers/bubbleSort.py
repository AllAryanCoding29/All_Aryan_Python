def bubblesort(arr):
    for i in range(amount):
        swapped = False
        for b in range(amount - i - 1):
            if array[b] > array[b+1]:
                array[b], array[b+1] = array[b+1], array[b]
                swapped = True
        if not swapped:
                break
    return arr
amount = int(input("Please enter the amount of values you wish to use: "))
array = []
for a in range(amount):
    num = int(input("Please enter each amount you wish in the array one by one : "))
    array.append(num)
print(array)
#print("Here is the bubblesorted edition : \n")
sortedarray = bubblesort(array)
print("Here is the bubble sorted array/list : ")
print(sortedarray)