from tkinter import messagebox
from tkinter import Label
from color_check import test
from tkinter import Tk
from tkinter import Canvas
from tkinter import Toplevel
from tkinter import Button

nb_color_in_line = 0

nb_tentative = 0

list_actual_color = []

color_check = []

#variable pour savoir si il faut définir le code secret
first_sequence = True

def set_result(dico, canva):
    '''
    Place les pions dans le canva en fonction du dictionaire fourni

    PARAMETRES:
    ------------------
    dico : dictionnaire
                    dico de 4 élements
    canva : tkinter Canvas
                canva dans lequel afficher les éléments

    SORTIE:
    --------
    Rien

    PRECONDITION:
    ------------------
    Le dictionaire dico doit contenir 4 éléments ni plus ni moins avec comme unique valeurs 0 / 1 / 2
    Sinon erreur
        
    POSTCONDITION:
    ------------------
    Si une valeur est égal à 0 dans le dictionaire aucun pion ne sera afficher
    '''
    import imports

    for j in range(len(dico)):
        if(dico[j] == 1):
            canva.create_image(385 + 50 * j, 34 + 70.25 * nb_tentative, image=imports.img_stick_noir)
        elif(dico[j] == 2):
            canva.create_image(385 + 50 * j, 34 + 70.25 * nb_tentative, image=imports.img_stick_blanc)



def essai(color, canva, window):
    '''
    Place les couleurs choisit par l'utilisateur sur le canva fournit et dans une liste

    PARAMETRES:
    ------------------
    color : string
                    argument principal : Choix possible : 
                     "reset" / "valider" / "del" / "vert / "bleu" / "orange" / "violet" / "gris" / "jaune" / "blanc" / "rouge"
    canva : tkinter Canvas
                canva dans lequel afficher les éléments
    window : instance de Tk()
                window dans laquelle afficher les éléments

    SORTIE:
    --------
    Rien : En fonction de l'argument la couleur est placé, "valider" valide la suite de 4 couleur, "del" la supprime pour en refaire une
    et "reset" relance le jeu (afin que l'utilisateur rechoisisse un code à faire deviner)
    Aucun élément retourné

    PRECONDITION:
    ------------------
    String color parmis la liste cité ci dessus sinon la fonction ne fera rien
    Instance de Tk() fonctionnelle
    Canva fonctionnel
    
    POSTCONDITION:
    ------------------
    "valider" nécessite 4 couleurs pas plus pas moins sinon une popup apparait
    "del" supprime toute la liste actuelle
    "reset" relance le jeu (l'utilisateur devra rechoisir un code couleur à faire deviner)
    L'utilisateur ne peut pas placer plus de 4 couleurs sinon une popup apparait
    '''
    from choose_code import create_popup_window, color_in_line, secret_code
    from victory_window import create_victory_window
    import imports

    global nb_color_in_line
    global nb_tentative
    global first_sequence

    #bool permettant de savoir si l'utilisateur doit choisir un code à faire deviner
    if(first_sequence == True):
        #si oui appel de la fonction pour choisir le code secret
        create_popup_window(window)
        return


    if(color == "reset"):
        if(canva != None):
            #reset des valeurs des variables, des listes, des éléments présents sur le canva + bool sur True pour rechoisir un code
            nb_color_in_line = 0
            nb_tentative = 0
            secret_code.clear()
            list_actual_color.clear()
            color_check.clear()
            first_sequence = True
            canva.delete("all")
            canva.create_image(345, 450, image=imports.bg_image)
            first_sequence = True
        return True
    if (color == "valider"):
        #appel de la fonction test pour comparer les listes
        if (nb_color_in_line != 4):
            #si il n'y a pas 4 couleurs choisit --> popup erreur
            messagebox.showerror("Erreur de jeu", "4 couleurs sont nécessaires pour valider la ligne !\n"
                                                  "Vous devez choisir 4 couleurs.\n")
            return
        #si le nombre de tentative excède 10 --> défaite (ici >= 9 puisque le nombre de tentative est modifié après cet vérification)
        result = test(secret_code, color_check)
        if(nb_tentative >= 9):
            #appel fonction pour créé la fenêtre de défaite / victoire
            create_victory_window(window, secret_code, False)
            #appel fonction pour placer les pions noirs et bancs grâce au dico retourné par la fonction test
            set_result(result, canva)
            #reset du jeu car défaite
            essai("reset", canva, window)
            return            
        if all(value == 1 for value in result.values()) == True:
            #appel fonction pour créé la fenêtre de défaite / victoire
            create_victory_window(window, secret_code, True)
            #appel fonction pour placer les pions noirs et bancs grâce au dico retourné par la fonction test
            set_result(result, canva)
            #reset du jeu car victoire
            essai("reset", canva, window)
            return
        else:
            #appel fonction pour placer les pions noirs et bancs grâce au dico retourné par la fonction test
            set_result(result, canva)
            nb_tentative += 1
            #clear des varibales + des listes des valeurs actuelles car utilisateur devra en saisir de nouvelles
            list_actual_color.clear()
            color_check.clear()
            nb_color_in_line = 0
            return
    if (color == "del"):
        #destroy des éléments du canva 
        for element in list_actual_color:
            canva.delete(element)
        #clear des varibales + des listes des valeurs actuelles car utilisateur devra en saisir de nouvelles
        list_actual_color.clear()
        color_check.clear()
        nb_color_in_line = 0
        return
    if (nb_color_in_line >= 4):
        #popup erreur si il y a plus de 4 couleurs choisit
        messagebox.showerror("Erreur de jeu", "Trop de couleur choisit !\nVous ne pouvez choisir que 4 couleurs par "
                                              "ligne maximum.\nPour changer la combinaison appuyer sur le boutton "
                                              "SUPPRIMER ")
        return False
    #en fontcion de la couleur donné en argument, le code place chaque couleur sur le canva en fonction de la variable color_in_line
    #ajout de la couleur et de l'élément actuel dans les listes color_code et list_actual_color
    if (color == "vert"):
        actual_color = canva.create_image(50 + 85 * nb_color_in_line, 34 + 70.25 * nb_tentative, image=imports.img_vert)
        list_actual_color.append(actual_color)
        color_check.append("vert")
    if (color == "bleu"):
        actual_color = canva.create_image(50 + 85 * nb_color_in_line, 34 + 70.25 * nb_tentative, image=imports.img_bleu)
        list_actual_color.append(actual_color)
        color_check.append("bleu")
    if (color == "orange"):
        actual_color = canva.create_image(50 + 85 * nb_color_in_line, 34 + 70.25 * nb_tentative, image=imports.img_orange)
        list_actual_color.append(actual_color)
        color_check.append("orange")
    if (color == "gris"):
        actual_color = canva.create_image(50 + 85 * nb_color_in_line, 34 + 70.25 * nb_tentative, image=imports.img_gris)
        list_actual_color.append(actual_color)
        color_check.append("gris")
    if (color == "rouge"):
        actual_color = canva.create_image(50 + 85 * nb_color_in_line, 34 + 70.25 * nb_tentative, image=imports.img_rouge)
        list_actual_color.append(actual_color)
        color_check.append("rouge")
    if (color == "violet"):
        actual_color = canva.create_image(50 + 85 * nb_color_in_line, 34 + 70.25 * nb_tentative, image=imports.img_violet)
        list_actual_color.append(actual_color)
        color_check.append("violet")
    if (color == "blanc"):
        actual_color = canva.create_image(50 + 85 * nb_color_in_line, 34 + 70.25 * nb_tentative, image=imports.img_blanc)
        list_actual_color.append(actual_color)
        color_check.append("blanc")
    if (color == "jaune"):
        actual_color = canva.create_image(50 + 85 * nb_color_in_line, 34 + 70.25 * nb_tentative, image=imports.img_jaune)
        list_actual_color.append(actual_color)
        color_check.append("jaune")
    nb_color_in_line += 1
    return True


#test unitaire vérifiant le bon fonctionnement de la fonction essai()
#aucune saisie utilisateur sur ce test, uniquement appel manuel pour vérifier si les couleurs et les pions sont bien placé
if(__name__ == '__main__'):

    first_sequence = False

    test_dico = {
    0: 1,
    1: 1,
    2: 2,
    3: 0
    }

    window = Tk()

    import imports

    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # find the center point
    center_x = int(screen_width / 2 - imports.WINDOW_WIDTH / 2)
    center_y = int(screen_height / 2 - imports.WINDOW_HEIGHT / 2)

    # set window size and center it
    window.geometry(f"{imports.WINDOW_WIDTH}x{imports.WINDOW_HEIGHT}+{center_x}+{center_y}")
    window.title("Mastermind")

    window.iconphoto(False, imports.img_icon)

    window['background'] = '#b97a57'

    window.resizable(False, False)

    bg_label = Label(image=imports.bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    canva = Canvas(window, width=690, height=890, highlightthickness=0)
    canva.pack()
    canva.create_image(345, 450, image=imports.bg_image)

    essai("vert", canva, window)
    essai("bleu", canva, window)
    essai("blanc", canva, window)
    essai("orange", canva, window)

    set_result(test_dico, canva)

    window.mainloop()

