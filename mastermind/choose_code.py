from tkinter import Toplevel
from tkinter import Label
from tkinter import Button
from tkinter import Tk
from tkinter import messagebox
import game

#initialisation des varibales

#nombre de couleur par ligne
color_in_line = 0 

#liste actuelle de couleur
list_actual_color = []

color_code = []

#liste contenant le code validé par l'utilisateur
secret_code = []

def init(color, window):
    '''
    Place les couleurs choisit par l'utilisateur sur la window fournit et dans une liste

    PARAMETRES:
    ------------------
    color : string
                    argument principal : Choix possible : 
                    "valider" / "del" / "vert / "bleu" / "orange" / "violet" / "gris" / "jaune" / "blanc" / "rouge"
    window : instance de Tk()
                window dans laquelle afficher les éléments

    SORTIE:
    --------
    Rien : En fonction de l'argument la couleur est placé, "valider" valide la suite de 4 couleur, "del" la supprime pour en refaire une
    Aucun élément retourné

    PRECONDITION:
    ------------------
    String color parmis la liste cité ci dessus sinon la fonction ne fera rien
    Instance de Tk() fonctionnelle
    
    POSTCONDITION:
    ------------------
    "valider" nécessite 4 couleurs pas plus pas moins sinon une popup apparait
    "del" supprime toute la liste actuelle
    L'utilisateur ne peut pas placer plus de 4 couleurs sinon une popup apparait
    '''

    import imports

    global color_in_line
    global secret_code

    if (color == "valider"):
        if (color_in_line != 4):
            #popup erreur apparait si il n'y a pas 4 couleur 
            messagebox.showerror("Erreur de jeu", "4 couleurs sont nécessaires pour valider la ligne !\n"
                                                  "Vous devez choisir 4 couleurs.\n")
            return
        else:
            #reset des valeurs des variables
            color_in_line = 0
            secret_code = color_code
            #bool pour savoir si il faut que l'utilisateur choisisse un code secret lors du début de parti
            game.first_sequence = False
            #destruction de la fenêtre
            window.destroy()
            return
    if (color == "del"):
        #clear de la liste des couleurs actuelle + reset variable + des images présentent sur la fenêtre
        for element in list_actual_color:
            element.after(5, element.destroy())
        list_actual_color.clear()
        color_code.clear()
        color_in_line = 0
        return
    if (color_in_line >= 4):
        #popup erreur si il y a plus de 4 couleurs choisit
        messagebox.showerror("Erreur de jeu", "Trop de couleur choisit !\nVous ne pouvez choisir que 4 couleurs par "
                                              "ligne maximum.\nPour changer la combinaison appuyer sur le boutton "
                                              "SUPPRIMER ")
        return
    #en fontcion de la couleur donné en argument, le code place chaque couleur en fonction de la variable color_in_line
    #ajout de la couleur et de l'élément actuel dans les listes color_code et list_actual_color
    if (color == "vert"):
        actual_color = Label(window, image=imports.img_vert, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=126)
        list_actual_color.append(actual_color)
        color_code.append("vert")
    if (color == "bleu"):
        actual_color = Label(window, image=imports.img_bleu, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=126)
        list_actual_color.append(actual_color)
        color_code.append("bleu")
    if (color == "orange"):
        actual_color = Label(window, image=imports.img_orange, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=126)
        list_actual_color.append(actual_color)
        color_code.append("orange")
    if (color == "gris"):
        actual_color = Label(window, image=imports.img_gris, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=126)
        list_actual_color.append(actual_color)
        color_code.append("gris")
    if (color == "rouge"):
        actual_color = Label(window, image=imports.img_rouge, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=126)
        list_actual_color.append(actual_color)
        color_code.append("rouge")
    if (color == "violet"):
        actual_color = Label(window, image=imports.img_violet, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=126)
        list_actual_color.append(actual_color)
        color_code.append("violet")
    if (color == "blanc"):
        actual_color = Label(window, image=imports.img_blanc, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=126)
        list_actual_color.append(actual_color)
        color_code.append("blanc")
    if (color == "jaune"):
        actual_color = Label(window, image=imports.img_jaune, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=126)
        list_actual_color.append(actual_color)
        color_code.append("jaune")
    #ajout 1 à color_in_line puisqu'une couleur a été choisit
    color_in_line += 1
    
    return

def create_popup_window(window):
    '''
    Initialise la fenêtre secondaire enfant de la fenêtre principale

    PARAMETRES:
    ------------------
    window : instance de Tk()
                fenêtre principale dont la secondaire va dépendre

    SORTIE:
    --------
    Rien : les éléments sont placés dans la fenêtre et celle ci est lancée.

    PRECONDITION:
    ------------------
    Instance de Tk() fonctionnelle
    
    POSTCONDITION:
    ------------------
    Rien
    '''

    import imports

    global color_in_line

    #création d'une nouvelle fenêtre par dessus la fenêtre principale 
    #titre + dimension + icone + background et autre paramètre propore à cette fenêtre
    new_window = Toplevel(window)
    new_window.title("Choix du code")
    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # find the center point
    center_x = int(screen_width / 2 - 700 / 2)
    center_y = int(screen_height / 2 - 300 / 2)
    new_window.geometry(f"{700}x{300}+{center_x}+{center_y}")
    new_window.iconphoto(False, imports.img_icon)
    new_window['background'] = '#b97a57'
    new_window.resizable(False, False)

    #interdit l'utilisateur de quitter cette fenêtre et de cliquer sur la fenêtre principale --> évite des bugs permettant d'ouvrir plusieurs fois cette fenêtre
    new_window.grab_set()

    color_in_line = 0

    #texte via un Label Tkinter avec personalisation du texte
    text = Label(new_window, text="Choisissez le code couleur que le détective doit trouver : \nCliquez sur valider pour confirmer votre choix",
     bg="#b97a57", fg="#ff1004", cursor="dot", font=("Arial", 15))
    text.pack()
    text_rule = Label(new_window, text="Un pion noir équivaut à une couleur bien placé\nUn pion blanc équivaut à une couleur mal placé \nRien signifie que la couleur n'est pas présente",
     bg="#b97a57", fg="#13FF00", cursor="dot", font=("Arial", 13))
    text_rule.pack()

    #création des différents boutons pour choisir les couleurs et ou supprimer / valider
    button_vert = Button(new_window, image=imports.img_vert, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                         command=lambda: init("vert", new_window))
    button_bleu = Button(new_window, image=imports.img_bleu, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                         command=lambda: init("bleu",new_window))
    button_orange = Button(new_window, image=imports.img_orange, bg="#b97a57", activebackground="#b97a57", highlightthickness=0,
                           bd=0,
                           command=lambda: init("orange",new_window))
    button_gris = Button(new_window, image=imports.img_gris, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                         command=lambda: init("gris",new_window))
    button_rouge = Button(new_window, image=imports.img_rouge, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                          command=lambda: init("rouge",new_window))
    button_violet = Button(new_window, image=imports.img_violet, bg="#b97a57", activebackground="#b97a57", highlightthickness=0,
                           bd=0,
                           command=lambda: init("violet",new_window))
    button_blanc = Button(new_window, image=imports.img_blanc, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                          command=lambda: init("blanc",new_window))
    button_jaune = Button(new_window, image=imports.img_jaune, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                          command=lambda: init("jaune",new_window))
    button_del = Button(new_window, image=imports.img_del, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                        command=lambda: init("del", new_window))
    button_valider = Button(new_window, image=imports.img_valider, bg="#b97a57", activebackground="#b97a57", highlightthickness=0,
                            bd=0,
                            command=lambda: init("valider", new_window))

    #fonction pour placer les bouttons sur la fenêtre
    button_vert.place(x=3, y=216)
    button_bleu.place(x=(6 + 64), y=216)
    button_orange.place(x=(6 + 64)* 2, y=216)
    button_gris.place(x=(6 + 64)*3, y=216 )
    button_rouge.place(x=(6 + 64)*4, y=216)
    button_violet.place(x=(6 + 64)*5, y=216)
    button_jaune.place(x=(6 + 64)*6, y=216)
    button_blanc.place(x=(6 + 64)*7, y=216)
    button_del.place(x=(6 + 64)*8, y=216)
    button_valider.place(x=(6 + 64)*9, y=216)

    return new_window

#test unitaire en crééant une nouvelle instance de Tk() uniquement pour le test
if(__name__ == '__main__'):
    window = Tk()
    window.title("TEST UNITAIRE")
    label = Label(window, text="TEST \nUNITAIRE", font=("Arial", 20), fg="red")
    label.pack()
    create_popup_window(window)
    window.mainloop()
