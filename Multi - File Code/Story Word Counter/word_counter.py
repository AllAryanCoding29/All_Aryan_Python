def read_story():
    list_of_words = []
    with open("story.txt", "r") as file:
        for line in file:
            words = line.split()
            for i in range(len(words)):
                list_of_words.append(words[i])
        return list_of_words

def word_counter(list_of_words):
    return len(list_of_words)

def run():
    list_of_words = read_story()
    word_count = word_counter(list_of_words)
    return f"The story has {word_count} words."

def write(text):
    with open("word_count.txt", "w") as file:
        file.write(text)

word_count_text = run()
write(word_count_text)
