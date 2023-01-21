import os
import pickle
import sys
import time
from tkinter import *

window = Tk()
window.title("CSP Fighter - Player 2: Choose Character")
window.geometry("500x500")
c = Canvas(window, width=100, height=500)

# COMMANDS FOR BUTTON
def Return():
    os.system("python3 char1s.py")


def PLACEHOLDER():
    list = [
        "Placeholder",  # name
        "Fighter",  # class
        "50",  # def x/100 (50 default)
        "50",  # HP x/100 (50 default)
        "50",
    ]  # speed x/100 (50 default)
    # writes the list (^^^) to char1.txt for use later
    pickle.dump(list, open("char2.txt", "wb"))
    window.destroy()
    os.system("python Stage_select.py")


def NEVIL():
    list = [
        "Nevil",  # name
        "Ranged",  # class
        "20",  # def x/100 (50 default)
        "60",  # HP x/100 (50 default)
        "50",
    ]  # speed x/100 (50 default)
    # writes the list (^^^) to char1.txt for use later
    pickle.dump(list, open("char2.txt", "wb"))
    window.destroy()
    os.system("python Stage_select.py")


def DONALD():
    list = [
        "Donald",  # name
        "Tank",  # class
        "80",  # def x/100 (50 default)
        "70",  # HP x/100 (50 default)
        "30",
    ]  # speed x/100 (50 default)
    # writes the list (^^^) to char1.txt for use later
    pickle.dump(list, open("char2.txt", "wb"))
    window.destroy()
    os.system("python3 Stage_select.py")


# END COMMANDS


# NORMAL BUTTONS
back = Button(text="Back", command=Return)
back.place(x=10, y=10)
# END

# CLASS LABLES
c.create_text(35, 75, text="Fighters:", fill="black", font=("Helvetica 10 bold"))
c.create_text(35, 145, text="Rangers:", fill="black", font=("Helvetica 10 bold"))
c.create_text(40, 215, text="Tanks:", fill="black", font=("Helvetica 10 bold"))
c.create_text(40, 285, text="Close:", fill="black", font=("Helvetica 10 bold"))

# P1 CHARACTER SELECTED:
p1 = pickle.load(open("char1.txt", "rb"))

# IMAGE BUTTONS:

# Placeholder Character
if str(p1[0]) != "Placeholder":
    # ^^^checks if player 1 selected character
    click_btn = PhotoImage(file="pics/icons/Placeholder.png")
    button = Button(window, image=click_btn, command=PLACEHOLDER, height=50, width=50)
    button.place(x=70, y=50)

# Nevil Character
if str(p1[0]) != "Nevil":
    # ^^^checks if player 1 selected character
    click_btn2 = PhotoImage(file="pics/icons/Nevil.png")
    button2 = Button(window, image=click_btn2, command=NEVIL, height=50, width=50)
    button2.place(x=70, y=120)

# Donald?
if str(p1[0]) != "Donald":
    click_btn3 = PhotoImage(file="pics/icons/Donald.png")
    button3 = Button(window, image=click_btn3, command=DONALD, height=50, width=50)
    button3.place(x=70, y=190)
# END IMAGE BUTTONS

# MAINLOOP
c.place(x=0, y=0)
window.mainloop()
# END
