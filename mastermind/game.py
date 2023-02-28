from tkinter import messagebox
from tkinter import Label
from color_check import count_common_elements
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
    import imports

    for j in range(len(dico)):
        if(dico[j] == 1):
            canva.create_image(385 + 50 * j, 34 + 70.25 * nb_tentative, image=imports.img_stick_noir)
        elif(dico[j] == 2):
            canva.create_image(385 + 50 * j, 34 + 70.25 * nb_tentative, image=imports.img_stick_blanc)



def set_color(color, canva, window):
    from choose_code import create_popup_window, color_in_line, secret_code
    from victory_window import create_victory_window
    import imports

    global nb_color_in_line
    global nb_tentative
    global first_sequence

    if(first_sequence == True):
        create_popup_window(window)
        return


    if(color == "reset"):
        if(canva != None):
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
        if (nb_color_in_line != 4):
            messagebox.showerror("Erreur de jeu", "4 couleurs sont nécessaires pour valider la ligne !\n"
                                                  "Vous devez choisir 4 couleurs.\n")
            return False
        if(nb_tentative >= 12):
            messagebox.showerror("Perdu !", "Vous avez eu trop de tentatives échouées\n"
                                                "Le code était : AVEC UNE MAGNIFIQUE POP UP IMAGE DU CODE LA MTN FAUT LE FAIRE ET CE DERNIER CHECK COMPTE PAS.\n"
                                                  "Vous pouvez recommencez une partie.\n")
        result = count_common_elements(secret_code, color_check)
        if all(value == 1 for value in result.values()) == True:
            create_victory_window(window, secret_code)
            set_result(result, canva)
            set_color("reset", canva, window)
        else:
            set_result(result, canva)
            nb_tentative += 1
        list_actual_color.clear()
        color_check.clear()
        nb_color_in_line = 0
        return
    if (color == "del"):
        for element in list_actual_color:
            canva.delete(element)
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

if(__name__ == '__main__'):

    first_sequence = False

    test_dico = {
    0: 1,
    1: 1,
    2: 0,
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

    set_result(test_dico, canva)

    window.mainloop()

