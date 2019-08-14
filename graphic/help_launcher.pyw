from tkinter import *
from json import *
from datetime import datetime

def help_launcher():
    # FILE
    with open("file\\theme.json", "r") as theme:
        th = load(theme)

    # VARIABLE
    color1 = th["my_theme"]["bg"]
    color2 = th["my_theme"]["fg"]
    color3 = th["my_theme"]["ft"]
    
    tf = "consolas"
    window_help = Tk()
    date = datetime.now()

    text = "Si vous voulez afficher vos commandes raccourcis ou en \
ajouter, tapez 'ls' ou'list' puis tapez 'add' ou 'show' pour ajouter une \
commande ou les afficher"

    # WINDOW
    window_help.title("Help")
    window_help.iconbitmap("img\\launch.ico")
    window_help.resizable(False, False)
    window_help.configure(bg=color1)

    # FRAME
    footer_help = Frame(window_help, bg=color3)

    # LABEL
    lbl_title = Label(window_help, text="help".upper(), bg=color1, fg=color2,
                      font=tf)

    lbl_fr = Message(window_help, text=text, bg=color1, fg=color2,
                     font=(tf, 12))

    lbl_date = Label(footer_help, text=date.year, bg=color3,
                     fg=color2, font=tf)

    # PACK
    lbl_title.pack(anchor="center", fill="x")
    lbl_fr.pack(fill="x")

    lbl_date.pack(side="right", fill="x")
    footer_help.pack(side="bottom", fill="x")
    
    window_help.mainloop()

if __name__ == "__main__":
    help_launcher()