""" Calculator by using tkinter frame work """

from tkinter import *
window = Tk()
window.title("SM-CALCULATOR")
window.geometry("350x360")
window.iconbitmap(r'C:/Users/admin/Desktop/codes2/ikw/images/cal.ico')
window.resizable(False, False)
window.config(bg="#17161b")

firstno = IntVar()
secondno = IntVar()

# =======================================================================================================================

# FRAME

frame1 = Frame(window, background="#17161b")
frame1.grid(row=0, column=0)
frame3 = Frame(window, background="#17161b")
frame3.grid(row=1, column=0)

# =======================================================================================================================

#  CAL DEFINE

def add():
    firstno = e.get()
    global math
    math = 'addtion'
    global f
    f = int(firstno)
    e.delete(0, END)

def sub():
    firstno = e.get()
    global math
    math = 'subtraction'
    global f
    f = int(firstno)
    e.delete(0, END)

def multiply():
    firstno = e.get()
    global math
    math = 'multiply'
    global f
    f = int(firstno)
    e.delete(0, END)

def divide():
    firstno = e.get()
    global f
    global math
    math = 'divide'
    f = int(firstno)
    e.delete(0, END)

def sqroot():
    firstno = e.get()
    global f
    global math
    math = 'sqroot'
    f = int(firstno)
    e.delete(0, END)

def squr():
    firstno = e.get()
    global f
    global math
    math = 'squr'
    f = int(firstno)
    e.delete(0, END)

def cube():
    firstno = e.get()
    global f
    global math
    math = 'cube'
    f = int(firstno)
    e.delete(0, END)

def percentage():
    firstno = e.get()
    global f
    global math
    math = 'percentage'
    f = int(firstno)
    e.delete(0, END)

def equal():
    secondno = e.get()
    e.delete(0, END)
    if math == 'addtion':
        e.insert(0, f + int(secondno))
    elif math == 'subtraction':
        e.insert(0, f - int(secondno))
    elif math == 'multiply':
        e.insert(0, f * int(secondno))
    elif math == 'divide':
        e.insert(0, f / int(secondno))
    elif math == 'squr':
        e.insert(0, f ** 2)
    elif math == 'sqroot':
        e.insert(0, f ** 0.5)
    elif math == 'cube':
        e.insert(0, f ** 3)
    elif math == 'percentage':
        e.insert(0, f % int(secondno))

def clr():
    e.delete(0, END)

def sm(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

# =======================================================================================================================
# ENTRYBOX

e = Entry(frame1, font=('arial', 25), width=20)
e.grid(row=0, column=0)

# =======================================================================================================================

# NUMBER BUTTONS

btn1 = Button(frame3, text="1", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#2a2d36",
                      activebackground="limegreen", command=lambda: sm(1))
btn1.grid(row=4, column=0)
btn2 = Button(frame3, text="2", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#2a2d36",
                      activebackground="limegreen", command=lambda: sm(2))
btn2.grid(row=4, column=1)
btn3 = Button(frame3, text="3", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#2a2d36",
                      activebackground="limegreen", command=lambda: sm(3))
btn3.grid(row=4, column=2)
btn4 = Button(frame3, text="4", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#2a2d36",
                      activebackground="limegreen", command=lambda: sm(4))
btn4.grid(row=5, column=0)
btn5 = Button(frame3, text="5", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#2a2d36",
                      activebackground="limegreen", command=lambda: sm(5))
btn5.grid(row=5, column=1)
btn6 = Button(frame3, text="6", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#2a2d36",
                      activebackground="limegreen", command=lambda: sm(6))
btn6.grid(row=5, column=2)
btn7 = Button(frame3, text="7", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#2a2d36",
                      activebackground="limegreen", command=lambda: sm(7))
btn7.grid(row=6, column=0)
btn8 = Button(frame3, text="8", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#2a2d36",
                      activebackground="limegreen", command=lambda: sm(8))
btn8.grid(row=6, column=1)
btn9 = Button(frame3, text="9", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#2a2d36",
                      activebackground="limegreen", command=lambda: sm(9))
btn9.grid(row=6, column=2)
btn10 = Button(frame3, text="0", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#2a2d36",
                       activebackground="limegreen", command=lambda: sm(0))
btn10.grid(row=7, column=1)

# ======================================================================================================================

# SYMBOLS BUTTON

btn11 = Button(frame3, text="⌫", font=("arial", 15, "bold"), width=7, height=2, bg="#3697f5", fg="#fff", bd=1,
                       activebackground="limegreen", command=clr)
btn11.grid(row=7, column=0)
btn12 = Button(frame3, text="=", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#fe9037",
                       activebackground="limegreen", command=equal)
btn12.grid(row=7, column=2)
btn13 = Button(frame3, text="+", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#2a2d36",
                       activebackground="limegreen", command=add)
btn13.grid(row=6, column=12)
btn14 = Button(frame3, text="-", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#2a2d36",
                       activebackground="limegreen", command=sub)
btn14.grid(row=5, column=12)
btn15 = Button(frame3, text="X", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#2a2d36",
                       activebackground="limegreen", command=multiply)
btn15.grid(row=1, column=12)
btn16 = Button(frame3, text="÷", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#2a2d36",
                       activebackground="limegreen", command=divide)
btn16.grid(row=4, column=12)
btn17 = Button(frame3, text="x²", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#2a2d36",
                       activebackground="limegreen", command=squr)
btn17.grid(row=1, column=0)
btn18 = Button(frame3, text="√x", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#2a2d36",
                       activebackground="limegreen", command=sqroot)
btn18.grid(row=1, column=2)
btn17 = Button(frame3, text="x³", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#2a2d36",
                       activebackground="limegreen", command=cube)
btn17.grid(row=1, column=1)
btn19 = Button(frame3, text="%", font=("arial", 15, "bold"), width=7, height=2, bd=1, fg="#fff", bg="#2a2d36",
                       activebackground="limegreen", command=percentage)
btn19.grid(row=7, column=12)

window.mainloop()
