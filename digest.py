import pandas as pd
import os
import re
import labeling as l
from settings import *
from tkinter import filedialog



def choose_file():
    file_path = filedialog.askopenfilename()
    return file_path

def flip_credits_negative(row):
    if row["Transaction Type"] == "credit":
        return -row["Amount"]
    else:
        return row["Amount"]

def format_transactions(transactions):
    transactions["Date"] = pd.to_datetime(transactions["Date"])
    transactions["Amount"] = transactions.apply(flip_credits_negative, axis=1)

def digest():
    transactions = pd.read_csv(choose_file())
    format_transactions(transactions)
    transactions = transactions[transactions["Date"] > pd.to_datetime('2023-09-01')]
    #TODO compare to saved
    l.process(transactions.to_dict(orient="records"))

if __name__ == "__main__":
    digest()

