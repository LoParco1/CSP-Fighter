import os
import pickle
import sys
import time
from tkinter import *

window = Tk()
window.title("CSP Fighter - Stage Select")
window.geometry("500x500")

# COMMANDS FOR BUTTON
def OHIO():
    pickle.dump("Ohio", open("map.txt", "wb"))
    window.destroy()
    os.system("python3 fight.py")


def SUN():
    pickle.dump("Sun", open("map.txt", "wb"))
    window.destroy()
    os.system("python3 fight.py")


def amog():
    pickle.dump("moog", open("map.txt", "wb"))
    window.destroy()
    os.system("python3 fight.py")


# END COMMANDS


# IMAGE BUTTONS:

# Ohio Map
click_btn = PhotoImage(file="pics/icons/Ohio.png")
button = Button(window, image=click_btn, command=OHIO, height=100, width=100)
button.place(x=100, y=100)

# Gavin Map
click_btn2 = PhotoImage(file="pics/icons/Gavin.png")
button2 = Button(window, image=click_btn2, command=OHIO, height=100, width=100)
button2.place(x=200, y=100)

# Sun Map
click_btn3 = PhotoImage(file="pics/icons/download.png")
button3 = Button(window, image=click_btn3, command=SUN, height=100, width=100)
button3.place(x=300, y=100)

# Lemon Map
click_btn4 = PhotoImage(file="pics/icons/Lemon.png")
button4 = Button(window, image=click_btn4, command=OHIO, height=100, width=100)
button4.place(x=150, y=200)

# amogus Map
click_btn5 = PhotoImage(file="pics/icons/Amongus map.png")
button5 = Button(window, image=click_btn5, command=amog, height=100, width=100)
button5.place(x=250, y=200)

# END IMAGE BUTTONS

# PACKS AND MAINLOOP

window.mainloop()
# END
