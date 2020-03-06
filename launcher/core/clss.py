from json import dump, load
from os import startfile, system

from graphic import *


class Launcher:
    def __init__(self, command):
        self.command = command
        self.text = ""
        self.color = ""

    def execute_app(self):
        with open("../file/launcher.json", 'r') as js:
            self.data = load(js)

        FUNCTIONS = {"add": main_add,
                     "ls": main_show,
                     "help": help_launcher,
                     "about": about_launcher,
                     "exit": (system, "shutdown -p"),
                     "restart": (system, "net view")
                     }

        self.command = self.command.strip().lower()
        if self.command:
            for i in self.data:
                if self.command == i["lnk"] or self.command == i["app"]:
                    app = i["app"]
                    try:
                        startfile(i["cmd"])
                        self.text = f"lancement de {app}"
                        self.color = "green"

                    except:
                        self.text = f"erreur {app}"
                        self.color = "red"

            if self.command in FUNCTIONS:
                try:  # Open function without argument
                    FUNCTIONS[self.command]()

                except TypeError:  # Open function with argument
                    FUNCTIONS[self.command][0](FUNCTIONS[self.command][1])
        
            else:
                self.text = f"not found {self.command}, open with qwant ?"
                self.color = "#e55039"

        return {"text": self.text,
                "fg": self.color}

    def theme_change(self):
        with open("../file/settings.json", 'r') as settings:
            SETT = load(settings)

        for i in SETT["bg_theme"]:
            if SETT["my_theme"]["bg"] == SETT["bg_theme"]["black"]:
                SETT["my_theme"]["bg"] = SETT["bg_theme"]["white"]
                SETT["my_theme"]["fg"] = SETT["fg_theme"]["black"]
                SETT["my_theme"]["ft"] = SETT["bg_theme"]["ft_white"]

            else:
                SETT["my_theme"]["bg"] = SETT["bg_theme"]["black"]
                SETT["my_theme"]["fg"] = SETT["fg_theme"]["white"]
                SETT["my_theme"]["ft"] = SETT["bg_theme"]["ft_black"]

            break

        with open("../file/settings.json", 'w') as save:
            dump(SETT, save, indent=4)
