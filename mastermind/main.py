from tkinter import PhotoImage
import os

ABSOLUTE_PATH = fr"{os.path.dirname(__file__)}/../img/"
print(ABSOLUTE_PATH)


def get_img(img_name):
    """
    color_name values : 
    "vert.png"
    "bleu.png"
    "orange.png"
    "gris.png"
    "rouge.png"
    "violet.png"
    "blanc.png"
    "jaune.png"
    "button_delet.png"
    "valider.png"
    "logo.png"
    "bg.png
    """
    try:
        img = PhotoImage(file=ABSOLUTE_PATH + "vert.png")
        print(fr"{ABSOLUTE_PATH} + 'vert.png'")
        return img
    except:
        print("Nom de fichier non valide")
        return False
