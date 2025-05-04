def sentence_input():
    input_sentence = input("Enter a sentence: ")
    return input_sentence.split() #Solve without using split

def word_counter():
    sentence = sentence_input()
    print(f"Here are the words in your sentence: {sentence}")
    i = 0
    while True:
        if i < len(sentence):
            i = i + 1
        else:
            print(f"The number of words in your sentence is {i}.")
            break

def restart():
    word_counter()
    r = input("Do you want to try again? Type enter to go again, and any other key to continue: ")
    if r == "":
        print("Ok!")
        restart()
    else:
        print("Thanks for trying My Sentence Counter!")
restart()