
filename = "transactions.txt"

def add_transaction(date, outgoing, incoming, amount, category):
    with open(filename, "a", encoding="utf=8") as f:
        f.write(date + ";" + outgoing + ";" + incoming + ";" + amount + ";" + category + ";\n")
        #adds an entry to the list seperating the columns by semicolons and the entries by lines.

def list_transactions():
    with open(filename, "r", encoding="utf=8") as f:
        print(f.read())
        #lists all the entries in the list

