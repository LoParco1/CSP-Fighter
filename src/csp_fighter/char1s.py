import os
import pickle
import sys
import time
from tkinter import *

window = Tk()
window.title("CSP Fighter - Player One: Choose Character")
window.geometry("500x500")
c = Canvas(window, width=100, height=500)


# COMMANDS FOR BUTTON
def Return():
    os.system("python3 main.py")


def PLACEHOLDER():
    list = [
        "Placeholder",  # name
        "Fighter",  # class
        "50",  # def x/100 (50 default)
        "50",  # HP x/100 (50 default)
        "50",
    ]  # speed x/100 (50 default)
    # writes the list (^^^) to char1.txt for use later
    pickle.dump(list, open("char1.txt", "wb"))
    window.destroy()
    os.system("python3 char2s.py")


def NEVIL():
    list = [
        "Nevil",  # name
        "Ranged",  # class
        "20",  # def x/100 (50 default)
        "60",  # HP x/100 (50 default)
        "50",
    ]  # speed x/100 (50 default)
    # writes the list (^^^) to char1.txt for use later
    pickle.dump(list, open("char1.txt", "wb"))
    window.destroy()
    os.system("python3 char2s.py")


def DONALD():
    list = [
        "Donald",  # name
        "Tank",  # class
        "80",  # def x/100 (50 default)
        "70",  # HP x/100 (50 default)
        "30",
    ]  # speed x/100 (50 default)
    # writes the list (^^^) to char1.txt for use later
    pickle.dump(list, open("char1.txt", "wb"))
    window.destroy()
    os.system("python3 char2s.py")


# def anotherperson():
# 	list = ["idk", #name
# 		"Close", #class
# 		"20", #def x/100 (50 default)
# 		"40",	#HP x/100 (50 default)
# 		"70"] #speed x/100 (50 default)
# 	#writes the list (^^^) to char1.txt for use later
# 	pickle.dump(list, open("char1.txt", "wb"))
# 	window.destroy()
# 	os.system('python3 char2s.py')

# END COMMANDS

# NORMAL BUTTON
back = Button(text="Back", command=Return)
back.place(x=10, y=10)
# END

# CLASS LABELS
c.create_text(35, 75, text="Fighters:", fill="black", font=("Helvetica 10 bold"))
c.create_text(35, 145, text="Rangers:", fill="black", font=("Helvetica 10 bold"))
c.create_text(40, 215, text="Tanks:", fill="black", font=("Helvetica 10 bold"))
c.create_text(40, 285, text="Close:", fill="black", font=("Helvetica 10 bold"))
# IMAGE BUTTONS:

# Placeholdr Character
click_btn = PhotoImage(file="pics/icons/Placeholder.png")
button = Button(window, image=click_btn, command=PLACEHOLDER, height=50, width=50)


# Nevil Character
click_btn2 = PhotoImage(file="pics/icons/Nevil.png")
button2 = Button(window, image=click_btn2, command=NEVIL, height=50, width=50)

# Donald?
click_btn3 = PhotoImage(file="pics/icons/Donald.png")
button3 = Button(window, image=click_btn3, command=DONALD, height=50, width=50)


# END IMAGE BUTTONS

# PACKS/PLACE AND MAINLOOP
c.place(x=0, y=0)
button.place(x=70, y=50)
button2.place(x=70, y=120)
button3.place(x=70, y=190)
window.mainloop()
# END
