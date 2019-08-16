from json import dump, load
from os import startfile, system

from graphic import *

class Launcher:
    def __init__(self, command):
        self.command = command
        self.text = ""
        self.color = ""

    def execute_app(self):
        with open("file\\run.json", 'r') as js:
            self.data = load(js)

        self.command = self.command.strip()
        for i in self.data:
            if self.command == "add":
                main_add()
                break
            
            elif self.command == "show":
                main_show()
                break

            elif self.command == "help":
                help_launcher()
                break

            elif self.command == "about":
                about_launcher()
                break

            elif self.command == "open":
                startfile("shortcuts")
                system("start %windir%\\explorer.exe shell:::\
{4234d49b-0245-4df3-b780-3893943456e1}")
                
                break

            elif self.command == "meteo":
                main_meteo()
                break

            elif self.command == "exit":
                exit()

            elif self.command == "shutdown":
                system("shutdown -p")
                break

            elif self.command == "restart":
                system("shutdown -r")
                break

            elif self.command == i["lnk"] or self.command == i["app"]:
                app = i["app"]
                try:
                    startfile(i["cmd"])
                    self.text = f"run {app}"
                    self.color = "green"

                except:
                    self.text = f"error {app}"
                    self.color = "red"

                break

            else:
                self.text = f"not found {self.command}"
                self.color = "orange"

        return {"text": self.text,
                "fg": self.color}

    def theme_change(self):
        with open("file\\theme.json", 'r') as th:
            self.theme = load(th)

        for i in self.theme["bg_theme"]:
            if self.theme["my_theme"]["bg"] == self.theme["bg_theme"]["black"]:
                self.theme["my_theme"]["bg"] = self.theme["bg_theme"]["white"]
                self.theme["my_theme"]["fg"] = self.theme["fg_theme"]["black"]
                self.theme["my_theme"]["ft"] = self.theme["bg_theme"]["ft_white"]

            else:
                self.theme["my_theme"]["bg"] = self.theme["bg_theme"]["black"]
                self.theme["my_theme"]["fg"] = self.theme["fg_theme"]["white"]
                self.theme["my_theme"]["ft"] = self.theme["bg_theme"]["ft_black"]

            break

        with open("file/theme.json", 'w') as save:
            dump(self.theme, save, indent=4)
