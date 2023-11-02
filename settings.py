from datetime import datetime
import csv

start_month = datetime(2023, 10, 1)
BUDGETS = [row for row in csv.DictReader(open("budgets/buckets.csv", mode="r")) if row.values]
LABELS = {row["key"]:row["name"] for row in BUDGETS}
TRANSACTIONS_DIR = "transactions"
###ui settings
DISPLAY_ROWS = 10
HEADING = ["Date", "Description", "Amount", "Account Name", "Category", "Budget Category"]