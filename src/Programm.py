filename = "transactions.txt"

def add_transaction(file,date, outgoing, incoming, amount, category):
    entry_string = date + ";" + outgoing + ";" + incoming + ";" + amount + ";" + category + ";\n"
    with open(file, "a", encoding="utf=8") as f:
        f.write(entry_string)
        #adds an entry to the list seperating the columns by semicolons and the entries by lines.
    return entry_string

def list_transactions(file):
    with open(file, "r", encoding="utf=8") as f:
        print(f.read())
    return 1
        #lists all the entries in the list

def ask_entry(): #Getting data from user and adding it to the list
    day = input("Insert day: ") #treating this as text as data treatment is not intended at the moment
    month = input("Insert month: ")
    year = input("Insert year: ")
    date = day + "/" + month + "/" + year
    outgoing = input("What's the outgoing account? ")
    incoming = input("What's the incoming account? ")
    amount = input("How much is being transfered? ")
    category = input("What category? ")
    add_transaction(filename,date, outgoing, incoming, amount, category)
    
def menu_selection():
    print("What do you want to do? \n" \
        "1 - add transaciton\n" \
        "2 - list all transactions recorded \n" \
        "other - quit")
    choice = input("Selection: ")
    if choice == '1':
        ask_entry()
        menu_selection()
    elif choice == '2':
        list_transactions()
        menu_selection()
    else:
        print("Goodbye")
        
if __name__ == '__main__':
    menu_selection()