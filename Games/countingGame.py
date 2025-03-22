print("Hello players, welcome to the counting game!")
print("To win, you must reach the number 50 first. You take turns adding 9 or less to the number, starting from 0.")
print("Example Game: 0,9,17,26,35,44,50!")
print("Game Begin!")
p1Name = input("Player 1, Enter your name! ")
p2Name = input("Player 2, Enter your Name! ")
p1Wins = 0
p2Wins = 0
while(1):                                               # This while loop controls multiple games. 
    ctr = 0
    while(1):
        while (1):
            print(p1Name,"Input your number : ")
            i = int(input())
            if i > 0 and i < 10 :
                break
            print(p1Name, "Invalid Input..... Try Again! ")
        ctr = ctr+i
        print("Sum so far is :")
        print(ctr)
        if ctr >= 50:
            print(p1Name, "Wins!")
            p1Wins = p1Wins + 1
            break
        while (1):
            print(p2Name,"Input your number : ")
            i = int(input())
            if i > 0 and i < 10 :
                break
            print(p2Name, "Invalid Input..... Try Again! ")
        ctr = ctr +i
        print("Sum so far is :")
        print(ctr)
        if ctr >=50:
            print(p2Name, "Wins!")
            p2Wins = p2Wins + 1
            break
    print("Current Score Between Players :")
    print(p1Name, "Wins : ", p1Wins)        
    print(p2Name, "Wins : ", p2Wins)
    restart = input("Press 1 to continue playing and keep score, Press any other key to exit : ")
    if restart != "1":
        break
print("Thanks for playing My Counter Game. The winner of the counting olympics is : ")
if p1Wins > p2Wins:
    print(p1Name, "with a score of", p1Wins, "wins to", p2Name, "with a score of", p2Wins, "wins!")
elif p1Wins < p2Wins:
    print(p2Name, "with a score of", p2Wins, "wins to", p1Name, "with a score of", p1Wins, "wins!")
else:
    print("Both Players! There was a tie with each player winning having", p2Wins, "wins!")





























# restart = 0
# player = 0
# playertwo = 0
# while (restart < 2):
#    invalid = 1
#    i = 0
#    c = 0
#    while (i < 50):
#        c = i
#        invalid = 1
#        while (invalid < 2):
#            i = int(input("Player 1, please enter your number: "))
#            if i < c:
#                i = c
#                invalid = 1
#                break
#            elif i > c + 9:
#                i = c
#                invalid = 1
#                break
#            else:
#                invalid = 2
#                print(i)
#                break  
#        if i >= 50:
#            player = player + 1
#            print(p1Name, "wins\n")
#            print(p1Name, ": ", player, p2Name, ":", playertwo)
#            break
#        else:
#            c = i
#            invalid = 1
#            while (invalid < 2):
#                i = int(input("Player 2, please enter your number: "))
#                if i < c:
#                    i = c
#                    invalid = 1
#                elif i > c + 9:
#                    i = c
#                    invalid = 1
#                else:
#                    invalid = 2
#                    print(i)
#        if i >= 50:
#            playertwo = playertwo + 1
#            print(p2Name, "wins\n")
#            print(p1Name, ": ", player, p2Name, ": ", playertwo)
#            break
# restart = int(input("Enter 1 to have another game, Enter 2 to exit : "))
# print("Thank you for playing My Counting Game!")