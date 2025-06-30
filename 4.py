import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        chars = ""
        if var_letters.get():
            chars += string.ascii_letters
        if var_digits.get():
            chars += string.digits
        if var_symbols.get():
            chars += string.punctuation

        if not chars:
            output_label.config(text="Select at least one character type.")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        output_label.config(text=f"Password: {password}")
    except ValueError:
        output_label.config(text="Enter a valid length.")

root = tk.Tk()
root.title("Advanced Password Generator")

tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()

var_letters = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include Letters", variable=var_letters).pack()
tk.Checkbutton(root, text="Include Digits", variable=var_digits).pack()
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack()
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
