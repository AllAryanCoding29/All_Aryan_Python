from random import choice

def user_input():
    name_input = input("What's the name of the subject? ")
    place_input = input(f"Where were they? ")
    action_input = input("What were they doing? ")
    return name_input, place_input, action_input

def sentence_generator():
    time_gen = choice(["was", "is"])
    location_gen = choice(["at", "in", "to"])
    tbontb_gen = choice(["the", ""])
    return time_gen, location_gen, tbontb_gen

def restart():
    play_again = input("Press enter to go again, and any other key to exit!")
    return play_again

def story_generator():
    while True:
        name, place, action = user_input()
        time, location, tbontb = sentence_generator()
        print(f"{name} {time} {action} {location} {tbontb} {place}.")
        restarting = restart()
        if restarting == "":
            print("restarting...")
        else:
            print("Thanks for playing My Story Generator!")
            break

print("Hello, and welcome to My Story Generator!")
story_generator()

