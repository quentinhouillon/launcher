from tkinter.messagebox import showwarning
from json import load, dump

class Launcher:
    def __init__(self, command, lab_text):
        self.command = command
        self.lab_text = lab_text
        from os import getcwd, chdir; chdir(getcwd())

    def execute_app(self):
        with open("file/run.json", 'r') as js:
            self.data = load(js)

        for i in self.data:
            if self.command == i["lnk"] or self.command == i["app"]:
                try:
                    from os import startfile; startfile(i["cmd"])
                    self.lab_text.config(
                        text=f"run: {self.command}", fg="green")
                
                except:
                    self.lab_text.config(text=f"error: {self.command}",
                                         bg="black", fg="red")
                
                break
                
            
            else:
                self.lab_text.config(text=f"not found: {self.command}",
                                        bg="black", fg="red")
