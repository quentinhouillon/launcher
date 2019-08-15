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
    with open("file\\theme.json", "r") as theme:
        th = load(theme)

    # VARIABLE
    color1 = th["my_theme"]["bg"]
    color2 = th["my_theme"]["fg"]
    color3 = th["my_theme"]["ft"]

    tf = "consolas"
    date = datetime.now()

    #WINDOW
    window_meteo = Tk()
    window_meteo.title("meteo")
    window_meteo.iconbitmap("img\\launch.ico")
    window_meteo.geometry("350x250")
    window_meteo.minsize(350, 90)
    window_meteo.configure(bg=color1)

    #FRAME
    main_meteo = Frame(window_meteo, bg=color1)
    footer = Frame(window_meteo, bg=color3)

    #LABEL
    title = Label(main_meteo, text="Meteo\n", bg=color1, fg=color2,
            anchor="center", font=tf)

    answer = Text(
        window_meteo, bd=0, bg=color1, fg=color2, font=(tf, 8))
    
    lbl_date = Label(footer, text=f"{date.year} - w4rmux", bg=color3, fg=color2)

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
