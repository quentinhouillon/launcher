from tkinter import *
from json import dump, load
from datetime import datetime

window = Tk()

with open("file/theme.json", 'r') as th:
    theme = load(th)

color = theme["my_theme"]["bg"]
color2 = theme["my_theme"]["fg"]
color3 = theme["my_theme"]["ft"]

var_text = StringVar()
font_type = "consolas"
date = datetime.now()

def run(event):
    for i in theme["bg_theme"]:
        if e_input.get() == i:
            theme["my_theme"]["bg"] = e_input.get()

            if theme["my_theme"]["bg"] == theme["bg_theme"]["black"]:
                theme["my_theme"]["fg"] = theme["fg_theme"]["white"]
                theme["my_theme"]["ft"] = theme["bg_theme"]["ft_black"]
    
            else:
                theme["my_theme"]["fg"] = theme["fg_theme"]["black"]
                theme["my_theme"]["ft"] = theme["bg_theme"]["ft_white"]
    
    my_theme = theme["my_theme"]["bg"]
    response.config(text=f"background theme: {my_theme}")

    with open("file/theme.json", 'w') as save:
        dump(theme, save, indent=4)


#WINDOW
window.title("theme")
window.iconbitmap("img\\launch.ico")
window.geometry("350x90")
window.minsize(350, 90)
window.configure(bg=color, cursor="pirate")

#FRAME
main = Frame(window, bg=color)
footer = Frame(window, bg=color3)

#LABEL
title = Label(main, text="background theme launcher", bg=color, fg=color2,
              anchor="center", font=(font_type, 15))

prompt = Label(main, text=">>", bg=color, fg=color2, font=font_type)
response = Label(window, bg=color, fg="green", font=(font_type, 8), anchor='w')
name = Label(footer, text=f"{date.year} - w4rmux", bg=color3, fg = color2, 
             font=(font_type, 8))

#ENTRY
e_input = Entry(main, bd=0, bg=color, fg=color2, insertbackground=color2,
		textvariable=var_text, font=font_type)

e_input.focus()
e_input.bind('<Return>', run)

#PACK
title.pack(fill='x')
prompt.pack(fill='x', side='left')
e_input.pack(fill='x')
main.pack(fill='both')

name.pack(side='right')
footer.pack(fill='x', side='bottom')

response.pack(fill='x')

if __name__ == "__main__":
    window.mainloop()
