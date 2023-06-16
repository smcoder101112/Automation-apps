""" 
This is the code for automating the whatsapp messages 
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

global k4
global k6
global k5

def search3():
    global k4
    global k6
    global k5
    url = "web.whatsapp.com"
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    webbrowser.register("chrome",NONE,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(url)
    time.sleep(75)
    pyautogui.click(283, 215) # contact search
    contact = k5.get()
    pyautogui.typewrite(contact) 
    time.sleep(30)
    pyautogui.click(185, 363) # contact click button
    time.sleep(20)
    n = int(k6.get())
    msg = k4.get()
    for i in range(n):
        pyautogui.click(699, 709)  # message type box
        time.sleep(0)
        pyautogui.typewrite(msg)
        time.sleep(1)
        pyautogui.click(1303, 702) # send button


d = Tk()
d.geometry("1366x768+0+0")
d.title("AutoMate WhatsApp")
d.state("zoomed")
d.iconbitmap(r'C:/Users/admin/Desktop/codes2/ikw/images/what.ico')
photo3 = ImageTk.PhotoImage(file=r'C:\Users\admin\Desktop\codes\ikw\images\bg1.jpg')
Label(d, image=photo3, height=768, width=1366).place(x=0, y=0)
k = Label(d, text="༒AUTOMATE WHATSAPP༒", relief=GROOVE, bd=12, fg="black", bg="white", width=24, height=1,
             font=("times new roman", 25))
k.place(x=150, y=30)
k1 = Label(d, text="MESSAGE", relief=GROOVE, bd=12, fg="#c1b5ca", bg="black", width=10, height=1,
               font=("italic", 20))
k1.place(x=60, y=200)
k2 = Label(d, text="REPEATION", relief=GROOVE, bd=12, fg="#c1b5ca", bg="black", width=10, height=1,
               font=("italic", 20))
k2.place(x=60, y=300)
k3 = Label(d, text="CONTACT", relief=GROOVE, bd=12, fg="#c1b5ca", bg="black", width=10, height=1,
               font=("italic", 20))
k3.place(x=60, y=400)
k4 = Entry(d, width=15, font=("italic", 20), relief=GROOVE, bd=12)
k4.place(x=250, y=200)
k5 = Entry(d, width=15, font=("italic", 20), relief=GROOVE, bd=12)
k5.place(x=250, y=400)

k6 = Spinbox(d, from_=0, to=1000, width=13, font=("italic", 20), relief=GROOVE, bd=12)
k6.place(x=250, y=300)

Button(d, text="SEND", bg="Slategray3", width=10, height=1, relief=GROOVE, bd=6, font=("arial", 20),
           activebackground="green4", command=search3).place(x=500, y=520)

d.mainloop()
