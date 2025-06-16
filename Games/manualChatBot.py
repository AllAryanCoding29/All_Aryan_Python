def chat_responses(question):
    if question == "How are you?":
        print("Great! Thanks for asking!")
        input("How about you? ")
    elif question == "What is your name?":
        print("I am ChatBot.")
        input("What's your name? ")
    elif question == "Tell me a joke: ":
        input("Why was the baseball stadium hot after the game? ")
        print("Because all the fans left.")
    else:
        print("I don't understand.")

print("Hello, I am Chatbot.")
while True:
    question_input = input("What do you want to ask? ")
    chat_responses(question_input)
    #change to dictionary