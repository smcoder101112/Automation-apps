""" Normal notepad using Tkinter frame work """

from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import font
from tkinter import scrolledtext

canvas=Tk()

canvas.geometry("1366x768")
canvas.title("NOTEPAD")
canvas.config(bg="white")
canvas.state("zoomed")
pikachu=Frame(canvas)
pikachu.pack(pady=0)


global selected
selected=False

def cut(e):
    global selected
    if e:
        selected = canvas.clipboard_get()
    else:
        if b5.selection_get():
            selected = b5.selection_get()
            b5.delete("sel.first", "sel.last")
            canvas.clipboard_clear()
            canvas.clipboard_append(selected)


def copy(e):
    global selected
    if e:
        selected=canvas.clipboard_get()
    else:
        if b5.selection_get():
            selected = b5.selection_get()
            canvas.clipboard_clear()
            canvas.clipboard_append(selected)


def paste(e):
    global selected
    if e:
        selected = canvas.clipboard_get()
    else:
        if selected:
            position = b5.index(INSERT)
            b5.insert(position, selected)


def undo():
    pass

def redo():
    pass

def savefile():
    newfile=asksaveasfile(mode= 'w', filetypes = [('text files','.txt')])
    if newfile is None:
        return
    text =str(b5.get(1.0,END))
    newfile.write(text)
    newfile.close()
    b5.delete(1.0, END)

def openfile():
    b5.delete(1.0, END)
    file = askopenfile(mode='r',filetypes= [('textfiles','*.txt')])
    if file is not None:
        content = file.read()
        b5.insert(INSERT,content)

def clearfile():
    b5.delete(1.0,END)

def new():
    b5.delete(1.0,END)
    canvas.title('newfile-Notepad!')
    b7.config(text="NEW File        ")

def color():
    b5 = colorchooser.askcolor()[1]
    canvas.config(bg=b5)

b5=scrolledtext.ScrolledText(canvas,undo=True,width=97,height=20,font=("poppins",20),bg="#ff8080",fg="black",wrap=WORD)
b5.pack()
b7= Label(canvas,text='smcoder        ',anchor=E)
b7.pack(fill=X,side=BOTTOM,ipady=5)

my_menu=Menu(canvas)
canvas.config(menu=my_menu)

file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New ",command=new )
file_menu.add_command(label="Open",command=openfile)
file_menu.add_command(label="Save",command=savefile)
file_menu.add_separator()
file_menu.add_command(label="Exit(alt + f4 )",command=canvas.quit)
edit_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",command=lambda: cut(False),accelerator="(ctrl+x)")
edit_menu.add_command(label="Copy",command=lambda: copy(False),accelerator="(ctrl+c)")
edit_menu.add_command(label="paste)",command=lambda: paste(False),accelerator="(ctrl+v)")
edit_menu.add_command(label="Clear All ",command=clearfile,accelerator="(ctrl+delete)")
edit_menu.add_separator()
edit_menu.add_command(label="undo",command=b5.edit_undo,accelerator="(ctrl+z)")
edit_menu.add_command(label="Redo",command=b5.edit_redo,accelerator="(ctrl+y)")


c_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Style",menu=c_menu)
c_menu.add_command(label="Background color",command=color)


canvas.bind('<Control-Key-x>',cut)
canvas.bind('<Control-Key-y>',copy)
canvas.bind('<Control-Key-z>',paste)
canvas.bind('<Control-Key-Delete>', clearfile)

canvas.mainloop()

"""
canvas = Toplevel(screen)
        canvas.geometry("1366x768")
        canvas.title("NOTEPAD")
        canvas.config(bg="white")

        def savefile():
            newfile = asksaveasfile(mode='w', filetypes=[('text files', '.txt')])
            if newfile is None:
                return
            text = str(b5.get(1.0, END))
            newfile.write(text)
            newfile.close()

        def openfile():
            file = askopenfile(mode='r', filetypes=[('textfiles', '*.txt')])
            if file is not None:
                content = file.read()
                b5.insert(INSERT, content)

        def clearfile():
            b5.delete(1.0, END)

        def exit():
            pass

        b1 = Button(canvas, text="Open", bg="Slategray3", width=15, height=1, bd=5, font=("arial", 10),
                    activebackground="firebrick4", command=openfile)
        b1.place(x=0, y=0)
        b2 = Button(canvas, text="save", bg="Slategray3", width=15, height=1, bd=5, font=("arial", 10),
                    activebackground="firebrick4", command=savefile)
        b2.place(x=130, y=0)
        b3 = Button(canvas, text="clear", bg="Slategray3", width=15, height=1, bd=5, font=("arial", 10),
                    activebackground="firebrick4", command=clearfile)
        b3.place(x=260, y=0)
        b4 = Button(canvas, text="exit", bg="Slategray3", width=15, height=1, bd=5, font=("arial", 10),
                    activebackground="firebrick4", command=exit)
        b4.place(x=390, y=0)
        b5 = Text(canvas, font=("poppins", 20), bg="#ff8080", fg="black", wrap=WORD)
        b5.place(x=0, y=30)
"""
