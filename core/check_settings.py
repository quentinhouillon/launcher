import sqlite3
from os import system, chdir, listdir
from json import dump

def check():
    try:
        chdir("file")

    except:
        system("mkdir file")
        chdir("file")

    if "Launcher.db" not in listdir("."):
        conn = sqlite3.connect("Launcher.db")
        cur = conn.cursor()

        cur.execute(
            """CREATE TABLE IF NOT EXISTS Launcher
               (id INTEGER PRIMARY KEY,
               shortcut TEXT NULL,
               opening TEXT NULL)""")

    if "theme.json" not in listdir("."):
        add_theme = {
            "dark": {
                "bg": "#181818",
                "fg": "white",
                "accent": "#2B2B2B"
            },
            "light": {
                "fg": "#a3adae",
                "fg": "black",
                "accent": "#d3d7d9",
            }
        }

        with open("theme.json", "w") as theme:
            dump(add_theme, theme, indent=4)
    
    if "config.json" not in listdir("."):
        add_config = {
            "settings": {
                "theme": "dark",
                "language": ""
            }
        }

        with open("config.json", "w") as config:
            dump(add_config, config, indent=4)
        
    # if "language.json" not in listdir("."):
    #     with open("language.json", "w") as language:
    #         pass

    chdir("..")
