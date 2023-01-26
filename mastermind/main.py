import tkinter as tk

window = tk.Tk()

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 480

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# find the center point
center_x = int(screen_width / 2 - WINDOW_WIDTH / 2)
center_y = int(screen_height / 2 - WINDOW_HEIGHT / 2)

# set window size and center it
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{center_x}+{center_y}")
window.title("Mastermind")

photo = tk.PhotoImage(file="..\\img\\logo.png")
window.iconphoto(False, photo)

window['background'] = '#6D6D6D'

window.resizable(False, False)

myCanvas = tk.Canvas(window)
myCanvas.pack()


def create_circle(x, y, r, canvas):  # center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    canvas.configure(bg="#6D6D6D")
    #faut set la size du canva sinon il est trop gros + son fond et sa bordure (set la size du canva dans cette fonction en fonction de la taille du cercle)
    return canvas.create_oval(x0, y0, x1, y1, fill="#FF0000")


create_circle(100, 100, 20, myCanvas)

window.mainloop()
