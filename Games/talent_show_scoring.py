class Participant:
    
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    
    def average_score(self):
        avg_score = sum(self.scores)/len(self.scores)
        return avg_score
    
    def result(self, avg_score):
        if avg_score >= 8:
            return "Qualified"
        else:
            return "Eliminated"
        

performer1 = Participant("Mohit", [7, 8, 9])
performer2 = Participant("Arjun", [6, 10, 9])
performer3 = Participant("Aryan", [10, 10, 10])
performer4 = Participant("Max", [4, 7, 8])

performers = [performer1, performer2, performer3, performer4]

for performer in performers:
    avg_score = performer.average_score()
    grade = performer.result(avg_score)
    print(f"{performer.name}'s scores are {performer.scores}. Their average was {avg_score:.2f} so they are {grade}.")

print("Congratulations to all performers, great work!")