
from tkinter import * #Used to create Windows
import pickle #Used to easily transfer data between files
import time #IDK Why we imported time
import sys
import os #Used to open new windows
pickle.dump(1,open("turn.txt","wb"))
pickle.dump(305,open("health.txt", "wb"))
pickle.dump(305,open("health2.txt", "wb"))
Print = print()

def play(): #Sends user to character select screen
    window.destroy()
    os.system('python char1s.py')
    #^^^a bit slower but works better

def settings(): #Opens setting window
  window.destroy()
  os.system('python Set.py')


def quit(): #Quits program
    window.destroy()




window = Tk()
window.title('CSP Fighter - Menu')
window.geometry("500x500")

#title in image
title = PhotoImage(file='Really Cool Logo.png')
img = Label(image=title)
img.pack()

#Buttons on home screen
play_bttn = Button(text="Start Game", command=play)
play_bttn.pack()

Settings = Button(text="Settings",
                  command=settings)
Settings.pack()

terminate = Button(text="Quit", command=quit)
terminate.pack()

window.mainloop()