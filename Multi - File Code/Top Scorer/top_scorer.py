def read_scores():
    items = {}
    with open("scores.txt", "r") as file:
        for line in file:
            words = line.split()
            items[words[0]] = int(words[1])
        return items

def find_highest_score():
    items = read_scores()
    name_of_topper = ""
    tv = 0
    for name, score in items.items():
        if score > tv:
            tv = score
            name_of_topper = name
    return name_of_topper, tv

def write_in_file(name, score):
    with open("top_scores.txt", "w") as file:
        file.write(f"{name} scored the highest with {score} marks.")

name, score = find_highest_score()
write_in_file(name, score)