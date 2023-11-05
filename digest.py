import pandas as pd
import os
import re
import labeling as l
from settings import *



def choose_file():
    transaction_files = os.listdir(TRANSACTIONS_DIR)
    transaction_files.sort()
    return TRANSACTIONS_DIR + "/" + transaction_files[0]

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
    l.process(transactions.to_dict(orient="records"))

if __name__ == "__main__":
    digest()

