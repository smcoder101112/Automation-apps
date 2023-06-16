""" 
This is the code for automating the instagram messages 
~ framework- tkinter
~ time management - time
~ automation-pyautogui 
~ web and image management - webbrowser
"""

from tkinter import *
from PIL import ImageTk
import pyautogui
import time
import webbrowser

global m4
global m6
global m5
   

def search4():
    global m4
    global m6
    global m5
    contact = m5.get()
    times = int(m6.get())
    messagee = m4.get()
    url = "https://www.instagram.com/accounts/login/"
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    webbrowser.register("chrome",NONE,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(url)
    time.sleep(30)
    pyautogui.click(944, 133)  # message box click
    time.sleep(2)
    pyautogui.click(523, 214)  # search
    time.sleep(2)
    pyautogui.typewrite(contact)
    time.sleep(2)
    pyautogui.click(818, 338)  # click at id
    time.sleep(2)
    pyautogui.click(830, 234)  # secondary message
    time.sleep(30)
    for i in range(times):
        pyautogui.click(663, 668)  # message entry click
        time.sleep(0)
        pyautogui.typewrite(messagee)
        time.sleep(1)
        pyautogui.click(1085, 665)  # message  send
        time.sleep(1)
        pyautogui.doubleClick(1070, 596)

h = Tk()
h.geometry("1366x768+0+0")
h.title("AutoMate INSTAGRAM")
h.state("zoomed")
h.iconbitmap(r'C:/Users/admin/Desktop/codes2/ikw/images/insta.ico')
photo3 = ImageTk.PhotoImage(file=r'C:\Users\admin\Desktop\codes\ikw\images\bg1.jpg')
Label(h, image=photo3, height=768, width=1366).place(x=0, y=0)
m = Label(h, text="༒AUTOMATE INSTAGRAM༒", relief=GROOVE, bd=12, fg="black", bg="white", width=24, height=1,
              font=("times new roman", 25))
m.place(x=150, y=30)
m1 = Label(h, text="MESSAGE", relief=GROOVE, bd=12, fg="#c1b5ca", bg="black", width=10, height=1,
               font=("italic", 20))
m1.place(x=60, y=200)
m2 = Label(h, text="REPEATION", relief=GROOVE, bd=12, fg="#c1b5ca", bg="black", width=10, height=1,
               font=("italic", 20))
m2.place(x=60, y=300)
m3 = Label(h, text="CONTACT", relief=GROOVE, bd=12, fg="#c1b5ca", bg="black", width=10, height=1,
               font=("italic", 20))
m3.place(x=60, y=400)
m4 = Entry(h, width=15, font=("italic", 20), relief=GROOVE, bd=12)
m4.place(x=250, y=200)
m5 = Entry(h, width=15, font=("italic", 20), relief=GROOVE, bd=12)
m5.place(x=250, y=400)

m6 = Spinbox(h, from_=0, to=1000, width=13, font=("italic", 20), relief=GROOVE, bd=12)
m6.place(x=250, y=300)


Button(h, text="SEND", bg="Slategray3", width=10, height=1, relief=GROOVE, bd=6, font=("arial", 20),
           activebackground="green4", command=search4).place(x=500, y=520)
h.mainloop()
