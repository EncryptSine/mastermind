from tkinter import Toplevel
from tkinter import Label
from tkinter import Button
from tkinter import Tk
from tkinter import messagebox
import game

color_in_line = 0

list_actual_color = []

color_code = []

secret_code = []

def set_color(color, window):

    import imports

    global color_in_line
    global secret_code

    if (color == "valider"):
        if (color_in_line != 4):
            messagebox.showerror("Erreur de jeu", "4 couleurs sont nécessaires pour valider la ligne !\n"
                                                  "Vous devez choisir 4 couleurs.\n")
            return
        else:
            color_in_line = 0
            secret_code = color_code
            game.first_sequence = False
            window.destroy()
            return
    if (color == "del"):
        for element in list_actual_color:
            element.after(5, element.destroy())
        list_actual_color.clear()
        color_code.clear()
        color_in_line = 0
        return
    if (color_in_line == 4):
        messagebox.showerror("Erreur de jeu", "Trop de couleur choisit !\nVous ne pouvez choisir que 4 couleurs par "
                                              "ligne maximum.\nPour changer la combinaison appuyer sur le boutton "
                                              "SUPPRIMER ")
        return
    if (color == "vert"):
        actual_color = Label(window, image=imports.img_vert, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=106)
        list_actual_color.append(actual_color)
        color_code.append("vert")
    if (color == "bleu"):
        actual_color = Label(window, image=imports.img_bleu, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=106)
        list_actual_color.append(actual_color)
        color_code.append("bleu")
    if (color == "orange"):
        actual_color = Label(window, image=imports.img_orange, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=106)
        list_actual_color.append(actual_color)
        color_code.append("orange")
    if (color == "gris"):
        actual_color = Label(window, image=imports.img_gris, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=106)
        list_actual_color.append(actual_color)
        color_code.append("gris")
    if (color == "rouge"):
        actual_color = Label(window, image=imports.img_rouge, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=106)
        list_actual_color.append(actual_color)
        color_code.append("rouge")
    if (color == "violet"):
        actual_color = Label(window, image=imports.img_violet, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=106)
        list_actual_color.append(actual_color)
        color_code.append("violet")
    if (color == "blanc"):
        actual_color = Label(window, image=imports.img_blanc, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=106)
        list_actual_color.append(actual_color)
        color_code.append("blanc")
    if (color == "jaune"):
        actual_color = Label(window, image=imports.img_jaune, bg="#b97a57", highlightthickness=0, bd=0)
        actual_color.place(x=180 + 85 * color_in_line, y=106)
        list_actual_color.append(actual_color)
        color_code.append("jaune")
    color_in_line += 1
    
    return True

def create_popup_window(window):

    import imports

    global color_in_line

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

    new_window.grab_set()

    color_in_line = 0

    text = Label(new_window, text="Choisissez le code couleur que le détective doit trouver : \n Cliquez sur valider pour confirmer votre choix",
     bg="#b97a57", fg="#ff1004", cursor="dot", font=("Arial", 15))
    text.pack()

    button_vert = Button(new_window, image=imports.img_vert, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                         command=lambda: set_color("vert", new_window))
    button_bleu = Button(new_window, image=imports.img_bleu, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                         command=lambda: set_color("bleu",new_window))
    button_orange = Button(new_window, image=imports.img_orange, bg="#b97a57", activebackground="#b97a57", highlightthickness=0,
                           bd=0,
                           command=lambda: set_color("orange",new_window))
    button_gris = Button(new_window, image=imports.img_gris, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                         command=lambda: set_color("gris",new_window))
    button_rouge = Button(new_window, image=imports.img_rouge, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                          command=lambda: set_color("rouge",new_window))
    button_violet = Button(new_window, image=imports.img_violet, bg="#b97a57", activebackground="#b97a57", highlightthickness=0,
                           bd=0,
                           command=lambda: set_color("violet",new_window))
    button_blanc = Button(new_window, image=imports.img_blanc, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                          command=lambda: set_color("blanc",new_window))
    button_jaune = Button(new_window, image=imports.img_jaune, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                          command=lambda: set_color("jaune",new_window))
    button_del = Button(new_window, image=imports.img_del, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                        command=lambda: set_color("del", new_window))
    button_valider = Button(new_window, image=imports.img_valider, bg="#b97a57", activebackground="#b97a57", highlightthickness=0,
                            bd=0,
                            command=lambda: set_color("valider", new_window))

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

if(__name__ == '__main__'):
    window = Tk()
    window.title("TEST UNITAIRE")
    label = Label(window, text="TEST \nUNITAIRE", font=("Arial", 20), fg="red")
    label.pack()
    create_popup_window(window)
    window.mainloop()
