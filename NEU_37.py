a = 5


def func():
    c = 10
    d = c + a

    globals()['a'] = d
    print(a)


func()




my_img1, my_img2, my_img3, my_img4, my_img5 = 20, 30, 40, 50, 60

image_list = [globals()[f"my_img{i}"] for i in range(1, 6)]
print(image_list)
print("----")
values = [21, 31, 41, 51, 61]
variables = {}

for i, value in enumerate(values, start=1):
    variables[f"my_img{i}"] = value

print(variables)
print(variables["my_img2"])

import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("240x100")
root.title('Login')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# username
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root,  show="*")
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# login button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


root.mainloop()
