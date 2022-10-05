# Generator
# Tiny and user-friendly random number generator written in Python3 using Tkinter GUI framework
# by Egor Komarov [https://github.com/MrErtor] and Ivan Movchan [https://github.com/NobootRecord]

# Import everything we need
from tkinter import * 
from tkinter import messagebox
import random
import webbrowser
from datetime import datetime

# Some variables
root = Tk()
inputFieldOne = None
inputFieldTwo = None
errorTitle = None
progver = "3.3"
light = 1
dark = 0
prog_theme = light

# Localization
eng = {"loc": "Generate number", "loc1": "Generator", 
"loc2": "Min value:", "loc3": "Max value",
"loc4": "The entered data is not correct", "loc5": "Input Error",
"loc6": "Help", "loc7": "About", "loc8": "Settings", "loc9": "Switch to Russian",
"loc10": "Generator "+progver+"\nWritten in Python3 using Tkinter framework\nAuthors: Egor Komarov, Ivan Movchan\n\nCopyright (c) 2022",
"loc11": "Dark/Light theme", "loc12": "Project on GitHub", "loc13": "Clear"}
rus = {"loc": "Сгенерировать число", "loc1": "Генератор",
"loc2": "Минимальное значение", "loc3": "Максимальное значение",
"loc4": "Введенные данные некорректны", "loc5": "Ошибка ввода",
"loc6": "Справка", "loc7": "О программе", "loc8": "Настройки", "loc9": "Сменить на Английский",
"loc10": "Генератор, версия "+progver+"\nПрограмма написана на Python3 с использованием фреймворка Tkinter\nАвторы: Егор Комаров, Иван Мовчан\n\nПрава сохранены (c) 2022",
"loc11": "Тёмная/светлая тема", "loc12": "Проект на GitHub", "loc13": "Очистить"}
lang_dict = eng
lang_dict["loc"]
is_eng = True

# Print current time
def print_time():
    now = datetime.now()
    asdasdf = now.strftime("[%D %H:%M:%S]")
    print(asdasdf, end=' ')

# On program close
def close_prog():
    print_time()
    print('The system is halted. Have a nice day!')
    exit()

# Generate random number
def btn_click():
    print_time()
    print('Generating random number')
    inputFieldOneValue = inputFieldOne.get()
    inputFieldTwoValue = inputFieldTwo.get()
    try:
        randomNum = random.randint(int(inputFieldOneValue), int(inputFieldTwoValue))
        info["text"] = info["text"] + str(randomNum) + ", "
    except ValueError:
        print_time()
        print('ValueError exception!!!')
        messagebox.showerror(title=lang_dict["loc5"], message=lang_dict["loc4"])

# Clear
def btn2_click():
    print_time()
    print('Clearing number label')
    info["text"] = ""

# Language change function
def change_lang():
    print_time()
    print('Switching program language')
    global is_eng
    global lang_dict
    is_eng = not is_eng
    if is_eng:
        lang_dict = eng
    else:
        lang_dict = rus
    update()
    
# Theme change function
def change_theme():
    print_time()
    print('Changing program theme')
    global prog_theme
    if prog_theme == light:
        prog_theme = dark
    elif prog_theme == dark:
        prog_theme = light
    init_gui()
        
# Initialize GUI
def init_gui():
    print_time()
    print('Initializing GUI')
    if prog_theme == light:
        formbg = "white"
        formfg = "black"
    if prog_theme == dark:
        formbg = "black"
        formfg = "white"
    root.title(lang_dict["loc1"])
    root.geometry("370x450")
    root.resizable(width=False, height=False)
    if prog_theme == light:
        color = "#eddda4"
    if prog_theme == dark:
        color = "#111144"
    rootmenu = Menu(root)
    root.config(menu = rootmenu, background = formbg)
    fm = Menu(rootmenu, tearoff = 0) 
    fm1 = Menu(rootmenu, tearoff = 0) 
    rootmenu.add_cascade(label = lang_dict["loc6"], menu = fm) # Help Menu
    fm.add_command(label = lang_dict["loc7"], command = about_click) # About...
    fm.add_command(label = lang_dict["loc12"], command = open_github) # GitHub
    rootmenu.add_cascade(label = lang_dict["loc8"], menu = fm1) # Settings Menu
    fm1.add_command(label = lang_dict["loc9"], command = change_lang) # Language
    fm1.add_command(label = lang_dict["loc11"], command = change_theme) # Theme
    frame = Frame(root, bg=formbg)
    frame.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.7)
    Label(frame, text=lang_dict["loc1"], bg=formbg, fg=formfg, font=("Comic Sans MS", 32)).pack()
    Label(frame, text="", bg=formbg, font=40).pack()
    Label(frame, text=lang_dict["loc2"], bg=formbg, fg=formfg, font=400).pack()
    global inputFieldOne
    inputFieldOne = Entry(frame, bg=color, fg=formfg)
    inputFieldOne.pack()
    Label(frame, text=lang_dict["loc3"], bg=formbg, fg=formfg, font=400).pack()
    global inputFieldTwo
    inputFieldTwo = Entry(frame, bg=color, fg=formfg)
    inputFieldTwo.pack()
    Label(frame, text="", bg=formbg, font=40).pack()
    frame_bottom = Frame(root, bg=color, bd=5)
    frame_bottom.place(relx=0.15, rely=0.70, relwidth=0.7, relheight=0.2)
    global info
    info = Label(frame_bottom, text=" ", bg=color, fg=formfg, font=40, wraplength=250, justify="center")
    info.bind("<Double-Button-1>", copy_to_clip)
    info.pack()
    Button(frame, text=lang_dict["loc"], bg=color, fg=formfg, command=btn_click).pack()
    Button(frame, text=lang_dict["loc13"], bg=color, fg=formfg, command=btn2_click).pack()
    root.protocol("WM_DELETE_WINDOW", close_prog)
    root.mainloop()

# GUI update function
def update():
        print_time()
        print('Updating')
        init_gui()
        
# About program
def about_click():
    print_time()
    print('Showing about messagebox')
    url = messagebox.showinfo(title=lang_dict["loc7"], message=lang_dict["loc10"])
    
# Open project's GitHub repository
def open_github():
    print_time()
    print('Opening project page on GitHub')
    webbrowser.open('https://github.com/MrErtor/generator')
    
# Copy generated number into clipboard
def copy_to_clip():
    print_time()
    print('Copying stuff into clipboard')
    root.clipboard_clear()
    root.clipboard_append(info["text"])
        
# Let's go!
print_time()
print('Generator', progver, 'initialized :)')
init_gui()