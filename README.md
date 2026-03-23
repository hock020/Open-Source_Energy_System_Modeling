# Open-Source_Energy_System_Modeling
This programme was build to simulate a very basic transaction recording programme. You can record transactions with a date, outgoing and incoming account, amount and category. 

## What does it do
There are four functions. 

* add_transaction(file,date, outgoing, incoming, amount, category): Does record a transaction into a file using semicolons as delimeters.
* list_transactions(file): Does output the files contents, i.e. the recorded transactions
* ask_entry(): Does the requesting of data from the user and using add_function records it in the file.
* menu_selection(): prints a menu and asks the user to choose. This allows the user to add a transaction to the ledger using ask_entry. The second option is to list the transactions using list_transactions. The finale usage case is to quit the program.

## Pytest

Pytest has been implemented and test file developed. However, only one function is tested there. This is due to the somewhat more complicated way to test file readings and writings. These are not really in my expertise at the moment.

## No AI has been used while performing this homework assignment.