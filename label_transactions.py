from tkinter import *
from tkinter import ttk
from settings import *

transaction_iter = []
labelled_transactions = []
current_transaction = {}

HEADING = ["Date", "Description", "Amount", "Account Name", "Category", "Budget Category"]

def display_data(t):
    return [t["Date"].strftime("%m/%d/%Y"), t["Description"], "${:.2f}".format(t["Amount"]), t["Account Name"], t["Category"], ""]

def process(list_of_transactions):

    def shift_rows(table):
        for i in range(1, DISPLAY_ROWS):
            fill_row(table[i], [c.cget("text") for c in table[i+1]])

    def budget_cat(budget_cat, current_transaction, row):

        row[-1].config(text=budget_cat)
        current_transaction[HEADING[-1]] = budget_cat

    def display_next_transaction(key):
        global current_transaction
        budget_cat(key, current_transaction, table[-1])
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
        display_next_transaction(key)

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

    table = create_table(root, rows=DISPLAY_ROWS+1, columns=len(HEADING))

    fill_row(table[0],HEADING)

    # Bind the key press event to the window
    root.bind("<Key>", key_press)
    # Start the main event loop
    root.mainloop()
        

