import tkinter as tk

t = range(10)
i = t.__iter__()

def key_press(event):
    key = event.keysym
    update_text(key)

def button_click():
    update_text()


def update_text(text=""):
    try: 
        new_text = str(i.__next__()) + " " + text
        label.config(text=new_text)
    except StopIteration:
        root.quit()

# Create the main window
root = tk.Tk()

root.geometry("400x300")

button = tk.Button(root, text="Next Transaction", command=button_click)
button.pack()
# Create a label widget with some text
label = tk.Label(root, text="Press any key to exit.")

# Pack the label widget to display it in the window
label.pack()

# Bind the key press event to the window
root.bind("<Key>", key_press)

# Start the main event loop
root.mainloop()

