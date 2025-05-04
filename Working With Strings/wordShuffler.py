import random

def shuffler(letters):
    list_of_letters = [char for char in letters]
    random.shuffle(list_of_letters)
    return ''.join(list_of_letters)

def run():
    word = input("What is your word? ")
    if len(word) <= 2:
        print("Word too short! Try Again!")
        run()
    else:
        shuffled_word = shuffler(word)
        print(shuffled_word)
        restart = input("Press enter to go again, and any other key to exit! ")
        if restart == "":
            print("Ok! Have Fun!")
            run()
        else:
            print("Thanks for using My Word Shuffler! ")

run()