from os import system
from tkinter import Label
from json import load, dump

class Launcher:
    def __init__(self, command, lab_text):
        self.command = command
        self.lab_text = lab_text
        from os import getcwd, chdir; chdir(getcwd())

    def execute_app(self):
        with open("file/run.json", 'r') as js:
            self.data = load(js)
        
        with open("file/theme.json", 'r') as th:
            self.theme = load(th)

        for i in self.data:
            if self.command == i["lnk"] or self.command == i["app"]:
                try:
                    from os import startfile; startfile(i["cmd"])
                    self.lab_text.config(
                        text=f"run: {self.command}",
                        bg=self.theme["my_theme"]["bg"], fg="green")

                except:
                    self.lab_text.config(text=f"error: {self.command}",
                                         bg=self.theme["my_theme"]["bg"],
                                         fg="red")
                
                break
            
            elif self.command == "exit":
                exit()
            
            elif self.command == "shutdown":
                system("shutdown -p")
            
            elif self.command == "restart":
                system("shutdown -r")
            
            else:
                self.lab_text.config(text=f"not found: {self.command}",
                                        bg=self.theme["my_theme"]["bg"],
                                        fg="red")
