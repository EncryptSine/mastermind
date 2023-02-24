from tkinter import Toplevel
from tkinter import Label
from tkinter import Tk
import game

color_in_line = 0



def set_color(color, window):

    import imports

    global color_in_line
    
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
    
    return True


def create_victory_window(window, code):

    import imports

    new_window = Toplevel(window)
    new_window.title("Vous avez gagné !")
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

    text = Label(new_window, text="Vous avez gagné la partie de mastermind en devinant le code couleur secret ! \n Pour relancer une partie fermez cette fenêtre.\n Le code était :",
     bg="#b97a57", fg="#ff1004", cursor="dot", font=("Arial", 15))
    text.pack()

    print(code)
    for element in code:
        print(element)
        set_color(element, new_window)

    return new_window

if(__name__ == '__main__'):
    window = Tk()
    window.title("TEST UNITAIRE")
    label = Label(window, text="TEST \nUNITAIRE", font=("Arial", 20), fg="red")
    label.pack()
    test_code = ["vert", "bleu", "orange", "jaune"]
    create_victory_window(window, test_code)
    window.mainloop()
