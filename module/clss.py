from tkinter.messagebox import showwarning
from os import system, chdir, getcwd

class Launcher:
    def __init__(self):
    	chdir(getcwd())
    
    def opening(self, app):
        try:
            system(f"start {app}")
        
        except:
            showwarning(
                "I don't understand !! \nEnter a true command")
    
    def execute_app(self, command):
        #site web

        if command.lower() == "qw" or command.lower() == "qwant":
            self.opening("https://www.qwant.com/")

        elif command.lower() == "ddg" or command.lower() == "duckduckgo":
            self.opening("https://start.duckduckgo.com")

        elif command.lower() == "g" or command.lower() == "google":
            self.opening("https://encrypted.google.com/")

        elif command.lower() == "yt" or command.lower() == "youtube":
            self.opening("https://www.youtube.com/")

        elif command.lower() == "nc" or command.lower() == "netcourrier":
            self.opening("https://www.netcourrier.com")

        elif command.lower() == "ent":
            self.opening("https://ent77.seine-et-marne.fr/auth/")

        elif command.lower() == "pr" or command.lower() == "pronote":
            self.opening(
                "https://0770009s.index-education.net/pronote/")

        elif command.lower() == "ub" or command.lower() == "ubisoft club":
            self.opening(
                "https://club.ubisoft.com/fr-FR/dashboard")

        elif command.lower() == "tk" or command.lower() == "tk docks":
            self.opening("http://www.tkdocs.com/tutorial/index.html")

        elif command.lower() == "ap" or command.lower() == "apprendre python":
            self.opening("https://apprendre-python.com")

        elif command.lower() == "d" or command.lower() == "developpez":
            self.opening("https://python.developpez.com/cours")

        elif command.lower() == "gnt" or command.lower() == "generation nt":
            self.opening("https://www.generation-nt.com/")

        elif command.lower() == "jg" or command.lower() == "journal du geek":
            self.opening("http://www.journaldugeek.com/")

        elif command.lower() == "pc" or command.lower() == "pc astuce":
            self.opening("http://pcastuce.com/")

        elif command.lower() == "cl" or command.lower() == "clubic":
            self.opening("http://clubic.com/")

        elif command.lower() == "w" or command.lower() == "whatsapp web":
            self.opening("https://web.whatsapp.com/")

# applications

        elif command.lower() == "ff" or command.lower() == "firefox":
            self.opening("firefox")

        elif command.lower() == "v" or command.lower() == "vivaldi":
            self.opening("vivaldi")

        elif command.lower() == "vsc" or command.lower() == "vs code":
            self.opening("code")

        elif command.lower() == "st" or command.lower() == "sublime text":
            self.opening("subl")

        elif command.lower() == "obs":
            self.opening("Shortuts/OBS.lnk")

        elif command.lower() == "py" or command.lower() == "python":
            self.opening("python")

        elif command.lower() == "cmd" or command.lower() == "invite de command.lower()":
            self.opening("cmd")

        elif command.lower() == "t" or command.lower() == "terminal":
            self.opening("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/\
Git/Git Bash.lnk")

        elif command.lower() == "cmder":
            self.opening("cmder")

        elif command.lower() == "po" or command.lower() == "powershell":
            self.opening("powershell")

        elif command.lower() == "cc" or command.lower() == "ccleaner":
            self.opening("ccleaner")

        elif command.lower() == "kp" or command.lower() == "keepass":
            self.opening("D:/Quentin/Documents/Database.kdbx")

        elif command.lower() == "idle":
            self.opening("C:/ProgramData/Microsoft/Windows/Start Menu/Programs\
/Python 3.6\IDLE (Python 3.6 32-bit)")

        elif command.lower() == "lo" or command.lower() == "libre office":
            self.opening("Shortuts/Lo.lnk")

        elif command.lower() == "gm" or command.lower() == "groove musique":
            self.opening("Shortuts/Gm.lnk")

        elif command.lower() == "mb" or command.lower() == "musicbee":
            self.opening("Shortuts/Mb.lnk")

        elif command.lower() == "c" or command.lower() == "courrier":
            self.opening("Shortuts/Co.lnk")

        elif command.lower() == "sk" or command.lower() == "skype":
            self.opening("Shortuts/Skype.lnk")

        elif command.lower() == "wa" or command.lower() == "whatsapp":
            self.opening("Shortuts/Wa.lnk")

        elif command.lower() == "dd" or command.lower() == "discord":
            self.opening("Shortuts/dd.lnk")

        elif command.lower() == "p" or command.lower() == "parametre":
            self.opening("Shortuts/Pa.lnk")

        elif command.lower() == "x" or command.lower() == "xbox":
            self.opening("Shortuts/Xb.lnk")

        elif command.lower() == "bn" or command.lower() == "bloc notes":
            self.opening("notepad")

        elif command.lower() == "ws" or command.lower() == "windows store":
            self.opening("Shortuts/St.lnk")

        elif command.lower() == "wd" or command.lower() == "windows defender":
            self.opening("Shortuts/Def.lnk")
        
        elif command.lower() == "ks" or command.lower() == "krapersky":
            self.opening("Shortuts/Ks.lnk")

        elif command.lower() == "wc" or command.lower() == "windows carte":
            self.opening("Shortuts/Map.lnk")

        elif command.lower() == "l" or command.lower() == "lecteur pdf":
            self.opening("Shortuts/Pdf.lnk")

        elif command.lower() == "wp" or command.lower() == "paint":
            self.opening("Shortuts/Paint.lnk")

        elif command.lower() == "gp" or command.lower() == "gimp":
            self.opening("Shortuts/GIMP.lnk")

        elif command.lower() == "cal" or command.lower() == "calculatrice":
            self.opening("C:/Users/Quentin/Documents/python/script_python/\
calculatrice.py")

        elif command.lower() == "cap" or command.lower() == "outil capture ecran":
            self.opening("Shortuts/screen.lnk")

        elif command.lower() == "b" or command.lower() == "battle.net":
            self.opening("Shortuts/Battle.lnk")

        elif command.lower() == "sc" or command.lower() == "shotcut":
            self.opening("Shortuts/shotcut.lnk")
        
        elif command.lower() == "exit":
            exit()
