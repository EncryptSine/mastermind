from tkinter import PhotoImage
import os

#fichier ou toutes les images sont importés
#à noter que pour que la fonction PhotoImage fonctionne, une instance de Tk() doit d'abord être créé

#récupération du path absolu du dossier image + constante de taille de la fenêtre
ABSOLUTE_PATH = fr"{os.path.dirname(__file__)}/../img/"
WINDOW_HEIGHT = 900
WINDOW_WIDTH = 700

img_icon = PhotoImage(file=ABSOLUTE_PATH + "logo.png")

bg_image = PhotoImage(file=ABSOLUTE_PATH + "bg.png")

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
img_reset = PhotoImage(file=ABSOLUTE_PATH + "reset.png")

img_stick_blanc = PhotoImage(file=ABSOLUTE_PATH + "baton_blanc.png")
img_stick_noir = PhotoImage(file=ABSOLUTE_PATH + "baton_noir.png")

#aucun test unitaire --> il s'agit juste d'importer les images que les autres fichiers utiliseront 