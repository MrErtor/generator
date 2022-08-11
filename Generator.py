# Generator
# Original by The.Ertor [https://github.com/MrErtor]
# Fixed by NobootRecord [https://github.com/NobootRecord]

# Import everything we need
from tkinter import * 
from tkinter import messagebox
import random
import webbrowser
import pyperclip

# Some variables
root = Tk()
inputFieldOne = None
inputFieldTwo = None
errorTitle = None
progver = "3.2"
light = 1
dark = 0
prog_theme = light

# Localization
eng = {"loc": "Generate number", "loc1": "Generator",  "loc2": "Enter the first number", "loc3": "Enter the second number", "loc4": "The entered value is not correct", "loc5": "Input Error", "loc6": "Help", "loc7": "About", "loc8": "Settings", "loc9": "Switch to Russian", "loc10": "Generator "+progver+"\nWritten in Python3 using Tkinter framework\n\nOriginal by The.Ertor\nFixed by NobootRecord\n\nCopyright (c) 2022", "loc11": "Dark/Light theme", "loc12": "Project on GitHub"}
rus = {"loc": "Сгенерировать число", "loc1": "Генератор", "loc2": "Введите первое число", "loc3": "Введите второе число", "loc4": "Введенное значение неверно", "loc5": "Ошибка ввода", "loc6": "Справка", "loc7": "О программе", "loc8": "Настройки", "loc9": "Сменить на Английский", "loc10": "Генератор, версия "+progver+"\nПрограмма написана на Python3 с использованием фреймворка Tkinter\n\nАвтор оригинала: The.Ertor\nДопилил и отполировал: NobootRecord\n\nCopyright (c) 2022", "loc11": "Тёмная/светлая тема", "loc12": "Проект на GitHub"}
lang_dict = eng
lang_dict["loc"]
is_eng = True


# Commands
def btn_click():
    inputFieldOneValue = inputFieldOne.get()
    inputFieldTwoValue = inputFieldTwo.get()
    try:
        randomNum = random.randint(int(inputFieldOneValue), int(inputFieldTwoValue))
        info["text"] = randomNum
    except ValueError:
        url = messagebox.showerror(title=lang_dict["loc5"], message=lang_dict["loc4"])

# Language change function
def change_lang():
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
    global prog_theme
    if prog_theme == light:
        prog_theme = dark
    elif prog_theme == dark:
        prog_theme = light
    init_gui()
        
# Initialize GUI
def init_gui():
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
    frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
    global title1
    title1 = Label(frame, text=lang_dict["loc1"], bg=formbg, fg=formfg, font=400) # Number Generator Text
    title1.pack()
    title2 = Label(frame, text="", bg=formbg, font=40)
    title2.pack()
    global title3
    title3 = Label(frame, text=lang_dict["loc2"], bg=formbg, fg=formfg, font=400) # Entering the first number
    title3.pack()
    global inputFieldOne
    inputFieldOne = Entry(frame, bg=color, fg=formfg)
    inputFieldOne.pack()
    global title4
    title4 = Label(frame, text=lang_dict["loc3"], bg=formbg, fg=formfg, font=400) # Entering the second number
    title4.pack()
    global inputFieldTwo
    inputFieldTwo = Entry(frame, bg=color, fg=formfg)
    inputFieldTwo.pack()
    title5 = Label(frame, text="", bg=formbg, font=40)
    title5.pack()
    frame_bottom = Frame(root, bg=color, bd=5)
    frame_bottom.place(relx=0.15, rely=0.70, relwidth=0.7, relheight=0.1)
    global info
    info = Label(frame_bottom, text=" ", bg=color, fg=formfg, font=40) # Number output
    info.bind("<Double-Button-1>", copy_to_clip)
    info.pack()
    global btn
    btn = Button(frame, text=lang_dict["loc"], bg=color, fg=formfg, command=btn_click) # Generate button Text
    btn.pack()
    root.mainloop()

# GUI update function
def update():
        btn["text"] = lang_dict["loc"]
        title1["text"] = lang_dict["loc1"]
        root.title(lang_dict["loc1"])   
        title3["text"] = lang_dict["loc2"]
        title4["text"] = lang_dict["loc3"]
        message = lang_dict["loc4"]
        title = lang_dict["loc5"]
        init_gui()
        
# Feature about user
def about_click(): 
    url = messagebox.showinfo(title=lang_dict["loc7"], message=lang_dict["loc10"])
    
# Open project's GitHub repository
def open_github():
    webbrowser.open('https://github.com/MrErtor/generator')
    
# Copy generated number into clipboard
def copy_to_clip(event):
    asdf = info.cget("text")
    if asdf != "":
        pyperclip.copy(asdf)
        
# Let's go!
init_gui()