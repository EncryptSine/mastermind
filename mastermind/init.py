from tkinter import *
from test import count_common_elements 
import game
import main

window = Tk()

WINDOW_HEIGHT = 900
WINDOW_WIDTH = 700

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# find the center point
center_x = int(screen_width / 2 - WINDOW_WIDTH / 2)
center_y = int(screen_height / 2 - WINDOW_HEIGHT / 2)

# set window size and center it
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{center_x}+{center_y}")
window.title("Mastermind")

photo = PhotoImage(file=main.get_img("logo.png"))
window.iconphoto(False, photo)

window['background'] = '#b97a57'

window.resizable(False, False)

bg_image = PhotoImage(file=main.get_img("bg.png"))
bg_label = Label(image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

nb_tentative = 0
nb_color_in_line = 0

# color = #be834f

button_1 = Button(window, image=main.get_img("img_vert"), bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                     command=lambda: game.set_color("vert"))
button_2 = Button(window, image=main.get_img("img_bleu"), bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                     command=lambda: game.set_color("bleu"))
button_3 = Button(window, image=main.get_img("img_orange"), bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                       command=lambda: game.set_color("orange"))
button_4 = Button(window, image=main.get_img("img_gris"), bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                     command=lambda: game.set_color("gris"))
button_5 = Button(window, image=main.get_img("img_rouge"), bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                      command=lambda: game.set_color("rouge"))
button_6 = Button(window, image=main.get_img("img_violet"), bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                       command=lambda: game.set_color("violet"))
button_7 = Button(window, image=main.get_img("img_blanc"), bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                      command=lambda: game.set_color("blanc"))
button_8 = Button(window, image=main.get_img("img_jaune"), bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                      command=lambda: game.set_color("jaune"))
button_del = Button(window, image=main.get_img("img_del"), bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                    command=lambda: game.set_color("del"))
button_valider = Button(window, image=main.get_img("img_valider"), bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                    command=lambda: game.set_color("valider"))

for i in range(8):
    eval("button_" + str(i + 1) + ".place(x=606, y=71 * " + str(i) + ")")
button_del.place(x=606, y=71 * 8)
button_valider.place(x=606, y=71 * 9)

window.mainloop()