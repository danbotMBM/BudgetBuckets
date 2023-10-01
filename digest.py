import pandas as pd
import os
import re
import label_transactions as lt
from settings import *



def choose_file():
    transaction_files = os.listdir(TRANSACTIONS_DIR)
    transaction_files.sort()
    return TRANSACTIONS_DIR + "/" + transaction_files[0]

def digest():
    transactions = pd.read_csv(choose_file())
    transactions["Date"] = pd.to_datetime(transactions["Date"])
    lt.process(transactions.to_dict(orient="records"))

if __name__ == "__main__":
    digest()

