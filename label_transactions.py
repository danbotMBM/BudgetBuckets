from datetime import datetime
import keyboard

def display_transaction(t):
    print(t["Date"].strftime("%m/%d/%Y"), t["Description"], "${:.2f}".format(t["Amount"]), t["Account Name"], t["Category"])

def process(list_of_transactions):
    print("printing transactions: (press space to continue)")
    for t in list_of_transactions:
        display_transaction(t)
        keyboard.wait("space")

