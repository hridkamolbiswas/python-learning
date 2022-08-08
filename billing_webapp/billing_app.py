#Import the required Libraries
from struct import pack
from tkinter import *
from tkinter import ttk

win = Tk()
#win.geometry("750x250")

header_frame = LabelFrame(win, width= 700, height= 180, bd=5)

header_frame_left = LabelFrame(header_frame, width=300, height=180, bd=5)
header_frame_right = LabelFrame(header_frame, width=100, height=180, bd=5)

mylabel_1 = Label(header_frame, text="Computer Arena")
mylabel_2 = Label(header_frame, text="Address1, address 2")


left_label = Label(header_frame_left, text="left-text-coulumn")



header_frame.pack()

left_label.pack()
mylabel_1.pack()
mylabel_2.pack()


header_frame_left.pack_propagate(False)
header_frame.pack_propagate(False)

win.mainloop()