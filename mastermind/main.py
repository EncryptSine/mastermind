from tkinter import *
import os

window = Tk()

WINDOW_HEIGHT = 900
WINDOW_WIDTH = 700
ABSOLUTE_PATH = fr"{os.path.dirname(__file__)}/../img/"

print(ABSOLUTE_PATH)

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# find the center point
center_x = int(screen_width / 2 - WINDOW_WIDTH / 2)
center_y = int(screen_height / 2 - WINDOW_HEIGHT / 2)

# set window size and center it
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{center_x}+{center_y}")
window.title("Mastermind")

photo = PhotoImage(file=ABSOLUTE_PATH + "logo.png")
window.iconphoto(False, photo)

window['background'] = '#b97a57'

window.resizable(False, False)

bg_image = PhotoImage(file=ABSOLUTE_PATH + "bg.png")
bg_label = Label(image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

nb_tentative = 0
nb_color_in_line = 0

# color = #be834f

nb_color_in_line = 0

list_actual_color = []


def set_color(color):
    global nb_color_in_line
    if (color == "del"):
        for element in list_actual_color:
            element.after(5, element.destroy())
        list_actual_color.clear()
        nb_color_in_line = 0
        print(nb_color_in_line)
        return
    if(nb_color_in_line == 4):
        print("TROP DE COULEURS CHOISIT FAUT FAIRE UN MESSAGE DERREUR")
        return False
    if (color == "vert"):
        actual_color = Label(window, image=img_vert, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=0, y=71 * nb_tentative)
        list_actual_color.append(actual_color)
    if (color == "bleu"):
        actual_color = Label(window, image=img_bleu, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=0, y=71 * nb_tentative)
        list_actual_color.append(actual_color)
    if (color == "orange"):
        actual_color = Label(window, image=img_orange, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=0, y=71 * nb_tentative)
        list_actual_color.append(actual_color)
    if (color == "gris"):
        actual_color = Label(window, image=img_gris, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=0, y=71 * nb_tentative)
        list_actual_color.append(actual_color)
    if (color == "rouge"):
        actual_color = Label(window, image=img_rouge, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=0, y=71 * nb_tentative)
        list_actual_color.append(actual_color)
    if (color == "violet"):
        actual_color = Label(window, image=img_violet, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=0, y=71 * nb_tentative)
        list_actual_color.append(actual_color)
    if (color == "blanc"):
        actual_color = Label(window, image=img_blanc, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=0, y=71 * nb_tentative)
        list_actual_color.append(actual_color)
    if (color == "jaune"):
        actual_color = Label(window, image=img_jaune, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=0, y=71 * nb_tentative)
        list_actual_color.append(actual_color)
    nb_color_in_line += 1

    print(nb_color_in_line)


img_vert = PhotoImage(file=ABSOLUTE_PATH + "vert.png")
img_bleu = PhotoImage(file=ABSOLUTE_PATH + "bleu.png")
img_orange = PhotoImage(file=ABSOLUTE_PATH + "orange.png")
img_gris = PhotoImage(file=ABSOLUTE_PATH + "gris.png")
img_rouge = PhotoImage(file=ABSOLUTE_PATH + "rouge.png")
img_violet = PhotoImage(file=ABSOLUTE_PATH + "violet.png")
img_blanc = PhotoImage(file=ABSOLUTE_PATH + "blanc.png")
img_jaune = PhotoImage(file=ABSOLUTE_PATH + "jaune.png")
img_del = PhotoImage(file=ABSOLUTE_PATH + "button_delet.png")

button_vert = Button(window, image=img_vert, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                     command=lambda: set_color("vert"))
button_bleu = Button(window, image=img_bleu, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                     command=lambda: set_color("bleu"))
button_orange = Button(window, image=img_orange, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                       command=lambda: set_color("orange"))
button_gris = Button(window, image=img_gris, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                     command=lambda: set_color("gris"))
button_rouge = Button(window, image=img_rouge, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                      command=lambda: set_color("rouge"))
button_violet = Button(window, image=img_violet, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                       command=lambda: set_color("violet"))
button_blanc = Button(window, image=img_blanc, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                      command=lambda: set_color("blanc"))
button_jaune = Button(window, image=img_jaune, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                      command=lambda: set_color("jaune"))
button_del = Button(window, image=img_del, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                    command=lambda: set_color("del"))

button_vert.place(x=606, y=0)
button_bleu.place(x=606, y=71)
button_orange.place(x=606, y=71 * 2)
button_gris.place(x=606, y=71 * 3)
button_rouge.place(x=606, y=71 * 4)
button_violet.place(x=606, y=71 * 5)
button_jaune.place(x=606, y=71 * 6)
button_blanc.place(x=606, y=71 * 7)
button_del.place(x=606, y=71 * 8)

window.mainloop()
