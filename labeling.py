from tkinter import *
from tkinter import ttk
from settings import *
import csv
from labeling_ui import run_ui

transactions = []
index = 0
input_buffer = []

def get_transaction(i):
    global transactions
    if i >= 0 and i < len(transactions):
        return transactions[i]
    return None

def categorize(transaction, cat):
    if transaction:
        transaction[HEADING[-1]] = cat

#add key to buffer. if matches a key empty buffer return category
def input_logic(key, input_display):
    global index, input_buffer
    if key == "BackSpace":
        if len(input_buffer) == 0 and index > 0:
            index -= 1
            transactions[index]["Budget Category"] = ""
        input_buffer.clear()
        string_input = "".join(input_buffer)
        input_display.config(text="INPUT: " + string_input)
        #refresh
        return True
    else:
        input_buffer.append(key)
    string_input = "".join(input_buffer)
    input_display.config(text="INPUT: " + string_input)   
    label = LABELS.get(string_input,"")
    if label:
        #label found categorize
        categorize(get_transaction(index), label)
        index += 1
        input_buffer.clear()
        #refresh
        return True
    #label did not match do not refresh
    return False

def process(list_of_transactions):
    global transactions 
    transactions = list_of_transactions
    run_ui()