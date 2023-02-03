from tkinter import *
import pickle
import time
import sys
import os

list = [305, 305]
pickle.dump("e", open("txt/Settings.txt", "wb"))
pickle.dump(list, open("txt/health.txt", "wb"))

def hpupdate():
	hp_current = hp[0]
	hp_current2 = hp[1]
	canvas.delete(HP1)
	canvas.delete(HP2)
	HP1 = canvas.create_rectangle(75, 10, 75 + hp_current, 50, fill="red")
	HP2 = canvas.create_rectangle(420 + hp_current2, 10, 420, 50, fill="red")

def attack():
    os.system('python moves.py')


def startgame(p1_hit_start, p2_hit_start, themap):
    global canvas
    global window
    global P1char
    global P2char
    global hp_current, hp_current2
    p1 = pickle.load(open("txt/char1.txt", "rb"))
    p2 = pickle.load(open("txt/char2.txt", "rb"))
    p12 = pickle.load(open("txt/char12.txt", "rb"))
    p22 = pickle.load(open("txt/char22.txt", "rb"))
    hp = pickle.load(open("txt/health.txt", "rb"))

    window = Tk()
    window.title('CSP Fighter - Fight!')
    window.geometry("900x600")

    canvas = Canvas(window, width=800, height=500)
    bg = PhotoImage(file="pics/bg/" + themap + "2.png")
    canvas.create_image(0, 0, image=bg, anchor="nw")

    #make characters
    x11 = 100
    x12 = 50

    x21 = 700
    x22 = 750

    y11 = 425
    y12 = 350

    y21 = 425
    y22 = 350
    #PLAYER 1
    p1icon = PhotoImage(file="pics/icons/" + p1[0] + ".png")
    icon1 = canvas.create_image(25, 25, image=p1icon)
    #first char p1
    P1charIMG = PhotoImage(file="pics/character/" + p1[0] + ".png")
    P1char = canvas.create_image(x11, y11, image=P1charIMG)
    #second char for p1
    P1charIMG2 = PhotoImage(file="pics/character/" + p12[0] + ".png")
    P1char2 = canvas.create_image(x12, y12, image=P1charIMG2)

    #PLAYER 2
    p2icon = PhotoImage(file="pics/icons/" + p2[0] + ".png")
    icon2 = canvas.create_image(775, 25, image=p2icon)
    #First char for p2
    P2charIMG = PhotoImage(file="pics/character/" + p2[0] + ".png")
    P2char = canvas.create_image(x21, y21, image=P2charIMG)
    #second char for p2
    P2charIMG2 = PhotoImage(file="pics/character/" + p22[0] + ".png")
    P2char2 = canvas.create_image(x22, y22, image=P2charIMG2)

    #HP bars
    hp_start = 305
    damage = 0
    damage2 = 0
    hp_current = hp[0]
    hp_current2 = hp[1]
    HP1bg = canvas.create_rectangle(73, 8, 382, 52, fill="gray")
    HP1 = canvas.create_rectangle(75, 10, 75 + hp_current, 50, fill="red")
    HP2bg = canvas.create_rectangle(727, 8, 418, 52, fill="gray")
    HP2 = canvas.create_rectangle(420 + hp_current2, 10, 420, 50, fill="red")
    start_bttn = Button(window, text="START", command=attack)
    #packs and mainloop
    canvas.pack()
    start_bttn.pack()
    window.mainloop()


map = pickle.load(open("txt/map.txt", "rb"))
startgame("x", "y", map)
