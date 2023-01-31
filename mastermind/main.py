import tkinter as tk

window = tk.Tk()

WINDOW_HEIGHT = 920
WINDOW_WIDTH = 720

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# find the center point
center_x = int(screen_width / 2 - WINDOW_WIDTH / 2)
center_y = int(screen_height / 2 - WINDOW_HEIGHT / 2)

# set window size and center it
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{center_x}+{center_y}")
window.title("Mastermind")

photo = tk.PhotoImage(file="P:\\NSI\\python\\mastermind\\mastermind\\img\\logo.png")
window.iconphoto(False, photo)

window['background'] = '#f0f0f0'

window.resizable(False, False)

absolute_path = "P:\\NSI\\python\\mastermind\\mastermind\\img\\"

img_path = [absolute_path + 'vert.png', absolute_path + 'bleu.png',absolute_path + 'orange.png',absolute_path + 'gris.png',absolute_path + 'rouge.png',absolute_path + 'violet.png', absolute_path + 'blanc.png', absolute_path + 'jaune.png', absolute_path + "button_delet.png"]
image_list = [tk.PhotoImage(file=x) for x in img_path]

i = 0
for item in image_list: # Number of rows
    for j in range(1): # Number of columns
        lbl = tk.Label(window,image=image_list[i])
        lbl.config
        lbl.grid(row=i,column=j)
    i += 1


window.mainloop()
