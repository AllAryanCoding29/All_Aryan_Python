def quote_reader():
    quotes = []
    with open("quotes.txt", "r") as file:
        for line in file:
            quotes.append(line)
        return quotes


def quote_reverser(quotes):
    reversed_quotes = []
    for quote in quotes:
        reversed_quotes.append(quote[::-1])
    return reversed_quotes

def run_and_write():
    quotes = quote_reader()
    reversed_quotes = quote_reverser(quotes)
    with open("reversed_quotes.txt", "w") as file:
        for i in range(0, len(reversed_quotes)):
            file.write(reversed_quotes[i])
    print("Process Completed!")

run_and_write()
#Make output remove the slash