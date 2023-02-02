import tkinter as tk
import os

window = tk.Tk()

WINDOW_HEIGHT = 920
WINDOW_WIDTH = 720
ABSOLUTE_PATH = fr"{os.path.dirname(__file__)}/../img/"

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# find the center point
center_x = int(screen_width / 2 - WINDOW_WIDTH / 2)
center_y = int(screen_height / 2 - WINDOW_HEIGHT / 2)

# set window size and center it
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{center_x}+{center_y}")
window.title("Mastermind")

photo = tk.PhotoImage(file=ABSOLUTE_PATH + "logo.png")
window.iconphoto(False, photo)

window['background'] = '#f0f0f0'

window.resizable(False, False)


def set_color(button):
    print(button)


button_dico = {"vert": "button0",
               "bleu": "button1",
               "orange": "button2",
               "gris": "button3",
               "rouge": "button4",
               "violet": "button5",
               "blanc": "button6",
               "jaune": "button7"}


GO FAIRE TOUT LES BUTTONS UN A UN CAR C GALERE JE SUIS PAS UN PRO DE LA POO PYTHON

image_list = [tk.PhotoImage(file=ABSOLUTE_PATH + x + ".png") for x in button_dico]

high = 0
j = 0
# GROS MANQUE D'OPTIMISATION MAIS CA MARCHE
for item in image_list:
    for j in range(1):  # Number of columns
        button = tk.Button(window, image=item)
        button.place(x=650, y=high)
        for key in button_dico:
            if button_dico[key] == "button" + str(j):
                button_dico[key] = button
            j += 1
    high += 70

print(button_dico)

window.mainloop()
