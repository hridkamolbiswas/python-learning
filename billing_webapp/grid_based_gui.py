from textwrap import fill
import tkinter as tk 
from tkinter import *
from tkinter import ttk

root = tk.Tk()
#root.geometry("750x400")
root.title("Computer Arena")
frame = tk.Frame()
frame.pack(expand=True)

# username
username_label = ttk.Label(frame, text="OrderID: 100100")
username_label.grid(row=0, column=0,  sticky=tk.NSEW, rowspan=3, padx=100, pady=5)


# header
header_label1 = ttk.Label(frame, text="Computer Arena")
header_label2 = ttk.Label(frame, text="Address1, address 2")
header_label3 = ttk.Label(frame, text="address3, address4")

header_label1.grid(row=0, column=1, padx=100, pady=5)
header_label2.grid(row=1, column=1, padx=100, pady=5)
header_label3.grid(row=2, column=1, padx=100, pady=5)

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', pady=10)
#separator.grid(row=3, column=0, columnspan=3, padx=100, pady=100, sticky=tk.W)

root.mainloop()
