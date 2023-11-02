from tkinter import *
from tkinter import ttk
from settings import *
import labeling

HEADING = ["Date", "Description", "Amount", "Account Name", "Category", "Budget Category"]
ROWS = DISPLAY_ROWS + 1
COLS = len(HEADING)


def row_display_data(t):
    if t:
        return [t["Date"].strftime("%m/%d/%Y"), t["Description"], "${:.2f}".format(t["Amount"]), t["Account Name"], t["Category"], t.get("Budget Category","")]
    else:
        return ["" for _ in HEADING]

def fill_row(row, contents):
    for i, c in enumerate(row):
        c.config(text=contents[i])

### passes back the keypress
def key_press(event, table, input_display):
    if labeling.input_logic(event.keysym, input_display):
        #if actual category update display table
        refresh_rows(table, labeling.index, labeling.transactions)


### Creates a tkinter table element of size ROWxCOLS and attaches it to the root frame
def create_table(root):
        # Create a table (2D list) to store Label widgets
        table = [[None for _ in range(COLS)] for _ in range(ROWS)]

        # Create Labels for each cell in the table
        for i in range(ROWS):
            for j in range(COLS):
                text = ""
                label = Label(root, text=text, relief="solid", borderwidth=1, width=15, height=2)
                label.grid(row=i, column=j)
                table[i][j] = label  # Store the Label widget in the table

        return table

### Refresh the table according to transaction position
def refresh_rows(table, transaction_index, transactions):
        position_of_labelling_transaction = DISPLAY_ROWS
        for k in range(1, DISPLAY_ROWS+1):
            i = transaction_index - position_of_labelling_transaction + k
            fill_row(table[k], [c for c in row_display_data(labeling.get_transaction(i))])

def run_ui():
    root = Tk()
    root.geometry("800x800")
    content = ttk.Frame(root)
    content.grid(column=0, row=0)
    #display input keys
    input_display = Label(root, text="INPUT: ")
    input_display.grid(row=DISPLAY_ROWS+2, column=0, columnspan=len(HEADING))
    i = 0
    for k, v in LABELS.items():
        key_legend = Label(root, text=v, width=15, height=1)
        key_legend.grid(row=DISPLAY_ROWS+3+i%10, column=0+(i//10*2), columnspan=1)
        key_legend = Label(root, text=k, width=15, height=1)
        key_legend.grid(row=DISPLAY_ROWS+3+i%10, column=1+(i//10*2), columnspan=1)
        i += 1
    table = create_table(root)
    fill_row(table[0], HEADING)
    refresh_rows(table, 0, labeling.transactions)
    # Bind the key press event to the window
    root.bind("<Key>", lambda event, table=table, input_display=input_display: key_press(event, table, input_display))
    # Start the main event loop
    root.mainloop()