from tkinter import *
from tkinter import messagebox
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

color_check = []

color_suit = ["vert", "bleu", "orange", "violet"]


def set_color(color):
    global nb_color_in_line
    global nb_tentative
    if (color == "valider"):
        if (nb_color_in_line != 4):
            messagebox.showerror("Erreur de jeu", "4 couleurs sont nécessaires pour valider la ligne !\n"
                                                  "Vous devez choisir 4 couleurs.\n")
            return False
        nb_tentative += 1
        nb_color_in_line = 0
        list_actual_color.clear()
        if (color_check == color_suit):
            print("GAGNE")
        color_check.clear()
        return
    if (color == "del"):
        for element in list_actual_color:
            element.after(5, element.destroy())
        list_actual_color.clear()
        color_check.clear()
        nb_color_in_line = 0
        return
    if (nb_color_in_line == 4):
        messagebox.showerror("Erreur de jeu", "Trop de couleur choisit !\nVous ne pouvez choisir que 4 couleurs par "
                                              "ligne maximum.\nPour changer la combinaison appuyer sur le boutton "
                                              "SUPPRIMER ")
        return False
    if (color == "vert"):
        actual_color = Label(window, image=img_vert, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=20 + 85 * nb_color_in_line, y=2 + 71 * nb_tentative)
        list_actual_color.append(actual_color)
        color_check.append("vert")
    if (color == "bleu"):
        actual_color = Label(window, image=img_bleu, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=20 + 85 * nb_color_in_line, y=2 + 71 * nb_tentative)
        list_actual_color.append(actual_color)
        color_check.append("bleu")
    if (color == "orange"):
        actual_color = Label(window, image=img_orange, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=20 + 85 * nb_color_in_line, y=2 + 71 * nb_tentative)
        list_actual_color.append(actual_color)
        color_check.append("orange")
    if (color == "gris"):
        actual_color = Label(window, image=img_gris, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=20 + 85 * nb_color_in_line, y=2 + 71 * nb_tentative)
        list_actual_color.append(actual_color)
        color_check.append("gris")
    if (color == "rouge"):
        actual_color = Label(window, image=img_rouge, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=20 + 85 * nb_color_in_line, y=2 + 71 * nb_tentative)
        list_actual_color.append(actual_color)
        color_check.append("rouge")
    if (color == "violet"):
        actual_color = Label(window, image=img_violet, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=20 + 85 * nb_color_in_line, y=2 + 71 * nb_tentative)
        list_actual_color.append(actual_color)
        color_check.append("violet")
    if (color == "blanc"):
        actual_color = Label(window, image=img_blanc, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=20 + 85 * nb_color_in_line, y=2 + 71 * nb_tentative)
        list_actual_color.append(actual_color)
        color_check.append("blanc")
    if (color == "jaune"):
        actual_color = Label(window, image=img_jaune, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=20 + 85 * nb_color_in_line, y=2 + 71 * nb_tentative)
        list_actual_color.append(actual_color)
        color_check.append("jaune")
    nb_color_in_line += 1
    return True


img_vert = PhotoImage(file=ABSOLUTE_PATH + "vert.png")
img_bleu = PhotoImage(file=ABSOLUTE_PATH + "bleu.png")
img_orange = PhotoImage(file=ABSOLUTE_PATH + "orange.png")
img_gris = PhotoImage(file=ABSOLUTE_PATH + "gris.png")
img_rouge = PhotoImage(file=ABSOLUTE_PATH + "rouge.png")
img_violet = PhotoImage(file=ABSOLUTE_PATH + "violet.png")
img_blanc = PhotoImage(file=ABSOLUTE_PATH + "blanc.png")
img_jaune = PhotoImage(file=ABSOLUTE_PATH + "jaune.png")
img_del = PhotoImage(file=ABSOLUTE_PATH + "button_delet.png")
img_valider = PhotoImage(file=ABSOLUTE_PATH + "valider.png")

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
button_valider = Button(window, image=img_valider, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                        command=lambda: set_color("valider"))

button_vert.place(x=606, y=0)
button_bleu.place(x=606, y=71)
button_orange.place(x=606, y=71 * 2)
button_gris.place(x=606, y=71 * 3)
button_rouge.place(x=606, y=71 * 4)
button_violet.place(x=606, y=71 * 5)
button_jaune.place(x=606, y=71 * 6)
button_blanc.place(x=606, y=71 * 7)
button_del.place(x=606, y=71 * 8)
button_valider.place(x=606, y=71 * 9)

window.mainloop()
