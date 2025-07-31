from datetime import date

def diary_entry():
    global date_of_entry
    entry = True
    diary_entry_processing = []
    diary_entry_processing.append(input("Begin writing your entry, press enter to go to the next line, and // on the end line to stop. "))
    while entry:
        diary_entry_processing.append(input(""))
        if "//" in diary_entry_processing:
            entry = False
            diary_entry_processing.remove("//")
            date_of_entry = date.today()
    with open("diary.txt", "a") as file:
        file.write(f"{date_of_entry} \n\n")
        for line in diary_entry_processing:
            file.write(f"{line}\n")

diary_entry()