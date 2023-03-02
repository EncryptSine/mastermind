from tkinter import Tk
from init import window_init

#création de l'instance principale de Tk()
#appel de la fonction pour initialiser la fenêtre principale
window = Tk()
window_init(window)

#pas de test unitaire --> fichier principal lançant le programme grâce à l'instance de Tk()