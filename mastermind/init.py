from tkinter import *
from tkinter import Tk


def init(window):
    import imports
    from game import set_color, first_sequence

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

    button_vert = Button(window, image=imports.img_vert, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                         command=lambda: set_color("vert", canva, window))
    button_bleu = Button(window, image=imports.img_bleu, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                         command=lambda: set_color("bleu", canva, window))
    button_orange = Button(window, image=imports.img_orange, bg="#b97a57", activebackground="#b97a57", highlightthickness=0,
                           bd=0,
                           command=lambda: set_color("orange", canva, window))
    button_gris = Button(window, image=imports.img_gris, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                         command=lambda: set_color("gris", canva, window))
    button_rouge = Button(window, image=imports.img_rouge, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                          command=lambda: set_color("rouge", canva, window))
    button_violet = Button(window, image=imports.img_violet, bg="#b97a57", activebackground="#b97a57", highlightthickness=0,
                           bd=0,
                           command=lambda: set_color("violet", canva, window))
    button_blanc = Button(window, image=imports.img_blanc, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                          command=lambda: set_color("blanc", canva, window))
    button_jaune = Button(window, image=imports.img_jaune, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                          command=lambda: set_color("jaune", canva, window))
    button_del = Button(window, image=imports.img_del, bg="#b97a57", activebackground="#b97a57", highlightthickness=0, bd=0,
                        command=lambda: set_color("del", canva, window))
    button_valider = Button(window, image=imports.img_valider, bg="#b97a57", activebackground="#b97a57", highlightthickness=0,
                            bd=0,
                            command=lambda: set_color("valider", canva, window))
    button_reset = Button(window, image=imports.img_reset, bg="#b97a57", activebackground="#b97a57", highlightthickness=0,
                            bd=0,
                            command=lambda: set_color("reset", canva, window))

    button_vert.place(x=606, y=1.5)
    button_bleu.place(x=606, y=71)
    button_orange.place(x=606, y=71 * 2)
    button_gris.place(x=606, y=71 * 3)
    button_rouge.place(x=606, y=71 * 4)
    button_violet.place(x=606, y=71 * 5)
    button_jaune.place(x=606, y=71 * 6)
    button_blanc.place(x=606, y=71 * 7)
    button_del.place(x=606, y=71 * 8)
    button_valider.place(x=606, y=71 * 9)
    button_reset.place(x=606, y=71 * 10)

    window.mainloop()

if __name__  == '__main__':
    init(window = Tk())