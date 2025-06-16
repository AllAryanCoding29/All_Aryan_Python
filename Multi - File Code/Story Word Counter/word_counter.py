def read_story():
    with open("story.txt", "r") as file:
        story = file.read()
        return story

def word_counter(story):
    words = story.split() #solve without split()
    return len(words)

def run():
    story_text = read_story()
    word_count = word_counter(story_text)
    print(f"The story has {word_count} words.")

run()
