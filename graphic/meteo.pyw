from tkinter import *
from json import load
from datetime import datetime
from bs4 import *
from requests import get

def main_meteo():
    # CALLBACK
    def _meteo(lbl):
        source = get(
            "http://www.meteofrance.com/previsions-meteo-france/tousson/77123")
        
        soup = BeautifulSoup(source.text, "lxml")

        for day in soup.find_all("div", class_="liste-jours"):
            day = day.text.strip()
            day = day.split("   ")

        for d in day:
            lbl.insert(INSERT, f" - {d}\n")

    # FILE
    with open("file\\settings.json", "r") as settings:
        SETT = load(settings)

    # VARIABLE
    COLOR1 = SETT["my_theme"]["bg"]
    COLOR2 = SETT["my_theme"]["fg"]
    COLOR3 = SETT["my_theme"]["ft"]

    TF = SETT["my_theme"]["font"]
    date = datetime.now()
    
    window_meteo = Tk()

    #WINDOW
    window_meteo.title("meteo")
    window_meteo.iconbitmap("img\\launch.ico")
    window_meteo.geometry("350x250")
    window_meteo.resizable(False, False)
    window_meteo.configure(bg=COLOR1, padx=5, pady=5)
    window_meteo.focus_force()

    #FRAME
    main_meteo = Frame(window_meteo, bg=COLOR1)
    footer = Frame(window_meteo, bg=COLOR3)

    #LABEL
    title = Label(main_meteo, text="Meteo\n", bg=COLOR1, fg=COLOR2,
            anchor="center", font=TF)

    answer = Text(
        window_meteo, bd=0, bg=COLOR1, fg=COLOR2, font=(TF, 8))
    
    lbl_date = Label(footer, text=f"{date.year} - w4rmux", bg=COLOR3, fg=COLOR2)

    # PACK
    title.pack(fill='x')
    main_meteo.pack(fill='both')

    lbl_date.pack(side="right")
    footer.pack(fill="x", side="bottom")

    answer.pack(fill="x")

    _meteo(answer)     
    window_meteo.mainloop()

if __name__ == "__main__":
    main_meteo()
