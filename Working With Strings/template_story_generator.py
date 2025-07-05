from random import randrange

def pizza_story():
    adjective = input("What kind of pizza was delivered? ")
    noun = input("Who's house was is delivered to? ")
    verb_pt = input("What did the delivery person do? ")
    place = input("Where did he leave it at? ")
    print(f"A {adjective} pizza was delivered to {noun}'s house. The delivery person {verb_pt} quickly and left it at the {place}.")


def pet_story():
    animal = input("What animal is your pet? ")
    verb = input("What does your pet do? ")
    adjective = input("Give a one word description of your pet: ")
    noun = input("What's your pet's favorite toy?")
    print(f"My pet {animal} likes to {verb} all day. It's very {adjective}, and its favorite toy is a {noun}.")


def flying_story():
    time = input("What time of day does the story occur? ")
    color = input("What color is the flying object? ")
    noun = input("What is the flying object? ")
    adverb = input("In what way was it flying? ")
    place = input("Where was it flying over? ")

    print(f"One {time}, I saw a {color} {noun} flying {adverb} over the {place}.")


def celebrity_story():
    name = input("Which celebrity is it? ")
    verb = input(f"What was {name} doing? ")
    adjective = input(f"What kind of person were they {verb} with? ")
    noun = input(f"Who was {name} {verb} with?")
    place = input("Where? ")
    emotion = input("How was the experience? ")
    print(f"The {name} decided to {verb} with a {adjective} {noun} in the {place}. It was a truly {emotion} experience!")

def template_picker():
    template = randrange(1,5)
    return template

def run():
    template = template_picker()
    if template == 1:
        print("I'm thinking we could do a pizza story.")
        pizza_story()
    elif template == 2:
        print("We could do a pet story!")
        pet_story()
    elif template == 3:
        print("We should do a flying story!")
        flying_story()
    else:
        print("I know! We could write a celebrity story!")
        celebrity_story()

run()
