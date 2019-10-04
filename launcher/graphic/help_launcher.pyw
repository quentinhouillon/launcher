from tkinter import *
from json import *
from datetime import datetime

def help_launcher():
    # FILE
    with open("../file/settings.json", "r") as settings:
        SETT = load(settings)

    # VARIABLE
    COLOR1 = SETT["my_theme"]["bg"]
    COLOR2 = SETT["my_theme"]["fg"]
    COLOR3 = SETT["my_theme"]["ft"]
    
    tf = "consolas"
    window_help = Tk()
    date = datetime.now()

    text = """
- tapez 'add' pour ajouter une commande d'ouverture ou 'ls' pour 
  les afficher.

- Launcher a besoin d'accéder au dossier 'shortcuts' qui contient
  tous les raccourcis. Pour y ajouter vos raccourcis, tapez 'open' puis
  glisser vos fichiers dans ce dossier.

- fonction 'add':
  Pour ajouter un site web, entrez juste
  l'url du site:
  exemple: 'https://www.google.com/';

  Pour une Application(dans le dossier 'shortcuts'), entrez
  juste le nom du fichier, exemple: 'firefox'

  Toute fois, vous pouvez utiliser le bouton 'parcourir' pour ouvrir un
  fichier qui ne se trouve pas dans le dossier 'shortcuts'

- Tapez 'meteo' dans Launcher, il vous donnera la météo

- Si vous saisissez une commande inconnue dans Launcher, un texte apparaîtra,
  cliquez sur celui-ci pour effectuer une recherche avec le moteur de 
  recherche qwant. """

    # WINDOW
    window_help.title("Help")
    window_help.iconbitmap("img\\launch.ico")
    window_help.resizable(False, False)
    window_help.configure(bg=COLOR1, padx=5, pady=5)
    window_help.focus_force()

    # FRAME
    footer_help = Frame(window_help, bg=COLOR3)

    # LABEL
    lbl_title = Label(window_help, text="help".upper(), bg=COLOR1, fg=COLOR2,
                      font=tf)

    lbl_fr = Message(window_help, text=text, bg=COLOR1, fg=COLOR2,
                     font=(tf, 12))

    lbl_date = Label(footer_help, text=date.year, bg=COLOR3,
                     fg=COLOR2, font=tf)

    # PACK
    lbl_title.pack(anchor="center", fill="x")
    lbl_fr.pack(fill="x")

    lbl_date.pack(side="right", fill="x")
    footer_help.pack(side="bottom", fill="x")
    
    window_help.mainloop()

if __name__ == "__main__":
    help_launcher()
