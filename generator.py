#!/usr/bin/python3
# See license.txt for licensing details.

WINDOW_TEXT = "Generator 3.4"
WINDOW_XSIZE, WINDOW_YSIZE = 480, 240
ENTRY_WIDTH = 40
XPADDING, YPADDING = 4, 8

HOMEPAGE = "https://github.com/MrErtor/generator"

try:
    from tkinter import *
    from tkinter import ttk
    import random, webbrowser
except ImportError:
    print("Failed to load some modules required by the application.")

window, min_value_box, max_value_box, out_box = None, None, None, None

def generate():
    min_str, max_str = min_value_box.get(), max_value_box.get()
    try:
        min_value, max_value = float(min_str), float(max_str)
        if min_value > max_value:
            min_value, max_value = max_value, min_value
            min_value_box.delete(0, END)
            max_value_box.delete(0, END)
            min_value_box.insert(0, max_str)
            max_value_box.insert(0, min_str)
        out_box.config(state=NORMAL)
        out_box.insert(1.0, str(random.uniform(min_value, max_value)) + "\n")
        out_box.config(state=DISABLED)
    except ValueError:
        print("Invalid data entered: \"%s\" and \"%s\"." % (min_str, max_str))

def clear():
    out_box.config(state=NORMAL)
    out_box.delete(1.0, END)
    out_box.config(state=DISABLED)

def copy_text():
    out_box.config(state=NORMAL)
    window.clipboard_clear()
    window.clipboard_append(out_box.get(1.0, "end-1c"))
    out_box.config(state=DISABLED)

def open_homepage():
    webbrowser.open(HOMEPAGE)

def app():
    global window
    window = Tk()
    
    WINDOW_XPOS = (window.winfo_screenwidth() / 2) - (WINDOW_XSIZE / 2)
    WINDOW_YPOS = (window.winfo_screenheight() / 2) - (WINDOW_YSIZE / 2)

    window.title(WINDOW_TEXT)
    window.geometry("%dx%d+%d+%d" % (
        WINDOW_XSIZE, WINDOW_YSIZE, WINDOW_XPOS, WINDOW_YPOS
    ))
    window.resizable(width=False, height=False)

    f1, f2 = Frame(), Frame()
    for f in [f1, f2]:
        f.pack(padx=XPADDING, pady=YPADDING, fill=X)

    global min_value_box, max_value_box
    min_value_box = ttk.Entry(f1, width=ENTRY_WIDTH)
    max_value_box = ttk.Entry(f1, width=ENTRY_WIDTH)
    min_value_box.pack(side=LEFT, padx=XPADDING, expand=1)
    max_value_box.pack(side=RIGHT, padx=XPADDING, expand=1)

    btn_generate = ttk.Button(f2, text="<<< Generate >>>", command=generate)
    btn_copy = ttk.Button(f2, text="Copy", command=copy_text)
    btn_clear = ttk.Button(f2, text="Clear", command=clear)
    btn_about = ttk.Button(f2, text="About...", command=open_homepage)
    btn_exit = ttk.Button(f2, text="Exit", command=window.destroy)

    for btn in [btn_generate, btn_copy, btn_clear, btn_about, btn_exit]:
        btn.pack(side=LEFT, padx=XPADDING, expand=1)

    global out_box
    out_box = Text(window, state=DISABLED)
    out_box.pack(side=LEFT, fill=BOTH, expand=1)

    window.mainloop()
    
if __name__ == "__main__":
    app()