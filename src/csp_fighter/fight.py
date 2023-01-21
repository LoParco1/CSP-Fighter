import os
import pickle
import sys
import time
import turtle
from pathlib import Path
from tkinter import *

p: Path = Path(os.path.realpath(__file__)).parent
char1_file: Path = Path.resolve(p / "char1.dat")
char2_file: Path = Path.resolve(p / "char2.dat")
map_file: Path = Path.resolve(p / "map.dat")

# BATTLE FUNCS
def p1jump(event):
    y = canvas.coords(P1char)[1]
    x = canvas.coords(P1char)[0]
    y += 5
    if y > 50:
        y -= 5


def p1down(event):
    y = canvas.coords(P1char)[1]
    x = canvas.coords(P1char)[0]
    y -= 5
    if y < 475:
        y += 5


def p2jump(event):
    y = canvas.coords(P2char)[1]
    x = canvas.coords(P2char)[0]
    y += 5
    if y > 50:
        y -= 5


def p2down(event):
    y = canvas.coords(P2char)[1]
    x = canvas.coords(P2char)[0]
    y -= 5
    if y < 475:
        y += 5


def p1right(event):
    y = canvas.coords(P1char)[1]
    x = canvas.coords(P1char)[0]
    x += 5
    if x > 775:
        x -= 5
    # CHECKS IF NEED TO FACE LEFT OR RIGHT
    if x > canvas.coords(P2char)[0]:
        print("face left")
    else:
        print("face right")
    canvas.coords(P1char, x, y)


def p1left(event):
    y = canvas.coords(P1char)[1]
    x = canvas.coords(P1char)[0]
    x -= 5
    if x < 25:
        x += 5
    # CHECKS IF NEED TO FACE LEFT OR RIGHT
    if x > canvas.coords(P2char)[0]:
        print("face left")
    else:
        print("face right")
    canvas.coords(P1char, x, y)


def p2right(event):
    y = canvas.coords(P2char)[1]
    x = canvas.coords(P2char)[0]
    x += 5
    if x > 775:
        x -= 5
    # CHECKS IF NEED TO FACE LEFT OR RIGHT
    if x > canvas.coords(P2char)[0]:
        print("face left")
    else:
        print("face right")
    canvas.coords(P2char, x, y)


def p2left(event):
    y = canvas.coords(P2char)[1]
    x = canvas.coords(P2char)[0]
    x -= 5
    if x < 25:
        x += 5
    # CHECKS IF NEED TO FACE LEFT OR RIGHT
    if x > canvas.coords(P2char)[0]:
        print("face left")
    else:
        print("face right")
    canvas.coords(P2char, x, y)


# END


def startgame(p1_hit_start, p2_hit_start, the_map):
    global canvas
    global window
    global P1char
    global P2char
    global HP1
    global HP2
    with char1_file.open("rb") as char1:
        p1 = pickle.load(char1)
        with char2_file.open("rb") as char2:
            p2 = pickle.load(char2)

            window = Tk()
            window.title("CSP Fighter - Fight!")
            window.geometry("800x500")
            wn = turtle.Screen()

            canvas = Canvas(window, width=800, height=500)
            bg = PhotoImage(file="pics/bg/" + the_map + "2.png")
            canvas.create_image(0, 0, image=bg, anchor="nw")

            # make characters
            p1icon = PhotoImage(file="pics/icons/" + str(p1[0] + ".png"))
            icon1 = canvas.create_image(25, 25, image=p1icon)
            P1charIMG = PhotoImage(file="pics/icons/" + str(p1[0] + ".png"))
            P1char = canvas.create_image(25, 475, image=P1charIMG)

            p2icon = PhotoImage(file="pics/icons/" + str(p2[0] + ".png"))
            icon2 = canvas.create_image(775, 25, image=p2icon)
            P2charIMG = PhotoImage(file="pics/icons/" + str(p2[0] + ".png"))
            P2char = canvas.create_image(775, 475, image=P2charIMG)
            # P2char = turtle.Turtle()
            # wn.addshape(name='pics/icons/'+str(p2[0])+".png",shape=None)
            # P2char.shape('pics/icons/'+str(p2[0])+".png")

            # HP bars
            HP1bg = canvas.create_rectangle(75, 8, 382, 52, fill="gray")
            HP1 = canvas.create_rectangle(75, 10, 380, 50, fill="red")
            HP2bg = canvas.create_rectangle(725, 8, 418, 52, fill="gray")
            HP2 = canvas.create_rectangle(725, 10, 420, 50, fill="red")

            # P1 controls
            window.bind("d", p1right)
            window.bind("a", p1left)
            window.bind("w", p1jump)
            window.bind("s", p1down)

            # P2 controls
            window.bind("<Left>", p2left)
            window.bind("<Right>", p2right)
            window.bind("<Up>", p2jump)
            window.bind("<Down>", p2down)

            # packs and mainloop
            canvas.pack()
            window.mainloop()


with map_file.open("rb") as _map:
    current_map = pickle.load(_map)

    startgame("x", "y", map)
