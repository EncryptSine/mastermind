from tkinter import Toplevel
from tkinter import Label
from tkinter import Tk
import game

color_in_line = 0

def set_color(color, window):
    '''
    Place les couleurs donné en argument dans la window.

    PARAMETRES:
    ------------------
    color : string
                    argument principal : Choix possible : 
                    "vert / "bleu" / "orange" / "violet" / "gris" / "jaune" / "blanc" / "rouge"
    window : instance de Tk()
                window dans laquelle afficher les éléments

    SORTIE:
    --------
    Rien : En fonction de l'argument la couleur est placé.
    Aucun élément retourné

    PRECONDITION:
    ------------------
    String color parmis la liste cité ci dessus sinon la fonction ne fera rien
    Instance de Tk() fonctionnelle
    
    POSTCONDITION:
    ------------------
    Rien
    '''

    import imports

    global color_in_line
    
    #en fontcion de la liste donné en argument, le code place chaque couleur sur la window en fonction de la variable color_in_line
    if (color == "vert"):
        actual_color = Label(window, image=imports.img_vert, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=126)
    if (color == "bleu"):
        actual_color = Label(window, image=imports.img_bleu, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=126)
    if (color == "orange"):
        actual_color = Label(window, image=imports.img_orange, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=126)
    if (color == "gris"):
        actual_color = Label(window, image=imports.img_gris, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=126)
    if (color == "rouge"):
        actual_color = Label(window, image=imports.img_rouge, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=126)
    if (color == "violet"):
        actual_color = Label(window, image=imports.img_violet, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=126)       
    if (color == "blanc"):
        actual_color = Label(window, image=imports.img_blanc, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=126)
    if (color == "jaune"):
        actual_color = Label(window, image=imports.img_jaune, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=126)
    color_in_line += 1
    
    return


def create_victory_window(window, code, bool):
    '''
    Initialise la fenêtre secondaire enfant de la fenêtre principale

    PARAMETRES:
    ------------------
    window : instance de Tk()
                fenêtre principale dont la secondaire va dépendre
    code : liste
                liste de string de 4 éléments contenant les couleurs du code secret 
                couleur possible : "jaune" / "violet" / "orange" / "blanc" / "gris" / "rouge" / "bleu" / "vert"
    bool = bool
                Booléen (True / False)

    SORTIE:
    --------
    new_window : la fenêtre créée avec les éléments placés dessus

    PRECONDITION:
    ------------------
    Instance de Tk() fonctionnelle
    Liste de 4 éléments pas plus ni moins
    
    POSTCONDITION:
    ------------------
    Si bool = True : La version victoire apparait
    Si bool = False : la version défaite apparait
    '''

    import imports

    global color_in_line

    #création d'une nouvelle fenêtre par dessus la fenêtre principale 
    #titre + dimension + icone + background et autre paramètre propore à cette fenêtre
    new_window = Toplevel(window)
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

    new_window.grab_set()

    #variable bool fournit : True = Victoire / False = Défaite
    #changement du texte et du titre de la fenêtre en fonction de bool
    if(bool == True):
        new_window.title("Vous avez gagné !")
        text = Label(new_window, text="Vous avez gagné la partie de mastermind en devinant le code couleur secret ! \n Pour relancer une partie fermez cette fenêtre.\n Le code était :",
        bg="#b97a57", fg="#ff1004", cursor="dot", font=("Arial", 15))
    elif(bool == False):
        new_window.title("Vous avez perdu !")
        text = Label(new_window, text="Vous avez perdu la partie de mastermind en faisant plus de 10 essaies incorrectes ! \n Pour relancer une partie fermez cette fenêtre.\n Le code était :",
        bg="#b97a57", fg="#ff1004", cursor="dot", font=("Arial", 13))
    
    text.pack()

    #code = liste de string des couleurs du code couleur 
    for element in code:
        #appel de la fonction pour placer les couleurs (element) de la liste
        set_color(element, new_window)
    
    color_in_line = 0

    return new_window

#test unitaire vérifiant le bon fonctionement de la fonction create_victory_window avec un code secret défini manuellement 
if(__name__ == '__main__'):
    window = Tk()
    window.title("TEST UNITAIRE")
    label = Label(window, text="TEST \nUNITAIRE", font=("Arial", 20), fg="red")
    label.pack()
    test_code = ["vert", "bleu", "orange", "jaune"]
    create_victory_window(window, test_code, False)
    window.mainloop()
