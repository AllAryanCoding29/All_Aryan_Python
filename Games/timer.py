import time
while True:
    totalMin = int(input("How many minutes do you want?"))
    while totalMin >= 0:
        hour = (totalMin // 60)
        minutes = (totalMin % 60)
        print(f"You have {hour} hours and {minutes} minutes")
        time.sleep(60)
        totalMin = totalMin - 1
    print("Time is up!")
    restart = input("Press 1 to restart, and Any other key to exit:")
    if restart == "1":
        continue
    else:
        print("Thanks for using My Timer!")
        break