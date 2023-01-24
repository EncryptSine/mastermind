from tkinter import *
from tkinter import ttk
 
window = Tk()
frm = ttk.Frame(window, padding=10)
window.geometry("480x720")
frm.grid()
window.resizable(False,False)
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
window.mainloop()