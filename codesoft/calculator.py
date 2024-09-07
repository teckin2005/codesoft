import tkinter as tk

# Function to update the input field when buttons are pressed
def button_click(event):
    current = input_field.get()
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(current)
            input_field.delete(0, tk.END)
            input_field.insert(tk.END, str(result))
        except Exception as e:
            input_field.delete(0, tk.END)
            input_field.insert(tk.END, "Error")
    elif text == "C":
        input_field.delete(0, tk.END)
    else:
        input_field.insert(tk.END, text)

# Creating the main tkinter window
root = tk.Tk()
root.title("Simple Calculator")

# Creating the input field
input_field = tk.Entry(root, font=("Arial", 18))
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# List of buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Adding buttons to the calculator
row = 1
col = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, font=("Arial", 14), width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", button_click)  # Binding click event
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()