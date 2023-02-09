from tkinter import messagebox
import main
from tkinter import *
import random
import test

nb_color_in_line = 0

list_actual_color = []

color_check = []

color = ["vert", "bleu", "orange", "gris", "rouge", "violet", "blanc", "jaune"]

color_suit = random.sample(color, 4)

def set_color(color, window):
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
        else: 
            print("FAUX")
            common_elements, same_position = test.count_common_elements(color_suit, color_check)
            print(f"Il y a {common_elements} éléments en commun entre les deux listes")
            print(f"{same_position} éléments se trouvent aux mêmes positions dans les deux listes")
            color_check.clear()
            f=0
            e=0
            while f < common_elements:
                print("pion noir")
                f += 1
            while e < same_position:
                print("pion blanc")
                e += 1
            
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
        actual_color = Label(window, image=main.img_vert, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=20 + 85 * nb_color_in_line, y=2 + 71 * nb_tentative)
        list_actual_color.append(actual_color)
        color_check.append("vert")
    if (color == "bleu"):
        actual_color = Label(window, image=main.img_bleu, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=20 + 85 * nb_color_in_line, y=2 + 71 * nb_tentative)
        list_actual_color.append(actual_color)
        color_check.append("bleu")
    if (color == "orange"):
        actual_color = Label(window, image=main.img_orange, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=20 + 85 * nb_color_in_line, y=2 + 71 * nb_tentative)
        list_actual_color.append(actual_color)
        color_check.append("orange")
    if (color == "gris"):
        actual_color = Label(window, image=main.img_gris, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=20 + 85 * nb_color_in_line, y=2 + 71 * nb_tentative)
        list_actual_color.append(actual_color)
        color_check.append("gris")
    if (color == "rouge"):
        actual_color = Label(window, image=main.img_rouge, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=20 + 85 * nb_color_in_line, y=2 + 71 * nb_tentative)
        list_actual_color.append(actual_color)
        color_check.append("rouge")
    if (color == "violet"):
        actual_color = Label(window, image=main.img_violet, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=20 + 85 * nb_color_in_line, y=2 + 71 * nb_tentative)
        list_actual_color.append(actual_color)
        color_check.append("violet")
    if (color == "blanc"):
        actual_color = Label(window, image=main.img_blanc, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=20 + 85 * nb_color_in_line, y=2 + 71 * nb_tentative)
        list_actual_color.append(actual_color)
        color_check.append("blanc")
    if (color == "jaune"):
        actual_color = Label(window, image=main.img_jaune, bg="red", highlightthickness=0, bd=0)
        actual_color.place(x=20 + 85 * nb_color_in_line, y=2 + 71 * nb_tentative)
        list_actual_color.append(actual_color)
        color_check.append("jaune")
    nb_color_in_line += 1
    
    print(color_check)
    return True