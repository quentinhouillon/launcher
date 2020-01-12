from os import system, chdir, listdir
from json import dump

def checking():
    try:
        chdir("../file")

    except:
        chdir("..")
        system("mkdir file")
        chdir("file")

    if "launcher.json" not in listdir("."):
        add_launcher = [
            {
                "app": "launcher",
                "lnk": "launcher",
                "cmd": "launcher.exe"
            },
        ]

        with open("launcher.json", "w") as launcher:
            dump(add_launcher, launcher, indent=4)
    
    if "apps_windows.json" not in listdir("."):
        add_apps = {
            "windows_apps": {
                "3D Builder": "com.microsoft.builder3d:",
                "Alarme et horloge": "ms-clock:",
                "Calculatrice": "calculator:",
                "Calendrier": "outlookcal:",
                "Caméra": "microsoft.windows.camera:",
                "Obtenir de l'aide": "ms-contact-support:",
                "Paramètres": "settings:",
                "groove musique": "mswindowsmusic:",
                "Courrier": "outlookmail:",
                "Carte": "bingmaps:",
                "Microsoft Edge": "microsoft-edge:",
                "Microsoft Store": "ms-windows-store:",
                "Film & Tv": "mswindowsvideo:",
                "Photos": "ms-photos:",
                "xbox": "xbox:"
            }
        }

        with open("apps_windows.json", 'w') as adder:
            dump(add_apps, adder, indent=4)

    if "settings.json" not in listdir("."):
        add_settings = {
            "bg_theme": {
                "black": "#181818",
                "white": "#a3adae",
                "ft_white": "#d3d7d9",
                "ft_black": "#2B2B2B"
            },
            "fg_theme": {
                "black": "black",
                "white": "white"
            },
            "my_theme": {
                "bg": "#181818",
                "fg": "white",
                "ft": "#2B2B2B",
                "font": "consolas"
            },
            "size": {
                "width": 350,
                "height": 120
            }
        }

        with open("settings.json", "w") as sett:
            dump(add_settings, sett, indent=4)
