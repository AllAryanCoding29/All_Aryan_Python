def read_story():
    with open("scores.txt", "r") as file:
        scores = file.read()
        return scores

def scores_dictionary(scores):
    scores = scores.split()
    return scores

read_scores = read_story()
print(scores_dictionary(read_scores))