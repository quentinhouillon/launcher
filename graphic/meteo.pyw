from tkinter import *
from json import load
from datetime import datetime
from bs4 import *
from requests import get

def meteo(lbl):
    source = get("http://www.meteofrance.com/previsions-meteo-france/tousson/77123").text

    soup = BeautifulSoup(source, "lxml")


    for day in soup.find_all("div", class_="liste-jours"):
        day = day.text.strip()
        day = day.split("   ")

    for d in day:
        lbl.insert(INSERT, f" - {d}\n")

def main():
    with open("file\\theme.json", 'r') as theme:
        th = load(theme)

    color1 = th["my_theme"]["bg"]
    color2 = th["my_theme"]["fg"]
    color3 = th["my_theme"]["ft"]

    font_type = "consolas"
    date = datetime.now()

    #WINDOW
    window = Tk()
    window.title("meteo")
    window.iconbitmap("img\\launch.ico")
    window.geometry("350x250")
    window.minsize(350, 90)
    window.configure(bg=color1, cursor="pirate")

    #FRAME
    main = Frame(window, bg=color1)
    footer = Frame(window, bg=color3)

    #LABEL
    title = Label(main, text="Meteo\n", bg=color1, fg=color2,
            anchor="center", font=font_type)

    answer = Text(
        window, bd=0, bg=color1, fg=color2, font=(font_type, 8))
    
    lbl_date = Label(footer, text=f"{date.year} - w4rmux", bg=color3, fg=color2)

    # PACK
    title.pack(fill='x')
    main.pack(fill='both')

    lbl_date.pack(side="right")
    footer.pack(fill="x", side="bottom")

    answer.pack(fill="x")
    meteo(answer) 
    
    window.mainloop()

main()
