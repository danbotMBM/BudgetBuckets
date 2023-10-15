from tkinter import *
from tkinter import ttk
from settings import *
import csv

transaction_iter = []
labelled_transactions = []
current_transaction = {}
input_buffer = []
BUDGETS = [row for row in csv.DictReader(open("budgets/buckets.csv", mode="r")) if row.values]
LABELS = {row["key"]:row["name"] for row in BUDGETS}

HEADING = ["Date", "Description", "Amount", "Account Name", "Category", "Budget Category"]

def display_data(t):
    return [t["Date"].strftime("%m/%d/%Y"), t["Description"], "${:.2f}".format(t["Amount"]), t["Account Name"], t["Category"], t.get("Budget Category","")]

def process(list_of_transactions):

    def shift_rows(table):
        for i in range(1, DISPLAY_ROWS):
            fill_row(table[i], [c.cget("text") for c in table[i+1]])

    #add key to buffer. if matches a key empty buffer return category
    def budget_cat(key):
        global input_buffer
        if key == "BackSpace":
            input_buffer.clear()
        else:
            input_buffer.append(key)
        string_input = "".join(input_buffer)
        input_display.config(text="INPUT: " + string_input)
        return LABELS.get(string_input,"")

    def categorize(transaction, cat):
        table[-1][-1].config(text=cat)
        transaction[HEADING[-1]] = cat
        labelled_transactions.append(transaction)

    def display_next_transaction():
        global current_transaction
        try:
            t = next(transaction_iter)
            current_transaction = t
            disp = display_data(t)
            shift_rows(table)
            fill_row(table[-1], disp)
        except StopIteration:
            root.quit()

    def fill_row(row, contents):
        for i, c in enumerate(row):
            c.config(text=contents[i])

    def key_press(event):
        key = event.keysym
        category = budget_cat(key)
        if category:
            input_buffer.clear()
            categorize(current_transaction, category)
            display_next_transaction()

    def create_table(root, rows, columns):
        # Create a table (2D list) to store Label widgets
        table = [[None for _ in range(columns)] for _ in range(rows)]

        # Create Labels for each cell in the table
        for i in range(rows):
            for j in range(columns):
                text = ""
                label = Label(root, text=text, relief="solid", borderwidth=1, width=15, height=2)
                label.grid(row=i, column=j)
                table[i][j] = label  # Store the Label widget in the table

        return table

    transaction_iter = iter(list_of_transactions)
    root = Tk()
    root.geometry("800x800")
    content = ttk.Frame(root)
    content.grid(column=0, row=0)
    input_display = Label(root, text="INPUT: ")
    input_display.grid(row=DISPLAY_ROWS+2, column=0, columnspan=len(HEADING))
    i = 0
    for k, v in LABELS.items():
        key_legend = Label(root, text=v, width=15, height=1)
        key_legend.grid(row=DISPLAY_ROWS+3+i%7, column=0+(i//7*2), columnspan=1)
        key_legend = Label(root, text=k, width=15, height=1)
        key_legend.grid(row=DISPLAY_ROWS+3+i%7, column=1+(i//7*2), columnspan=1)
        i +=1
    table = create_table(root, rows=DISPLAY_ROWS+1, columns=len(HEADING))

    fill_row(table[0],HEADING)
    display_next_transaction()
    # Bind the key press event to the window
    root.bind("<Key>", key_press)
    # Start the main event loop
    root.mainloop()
        

