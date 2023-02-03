from tkinter import *
import pickle
import time
import sys
import os

window = Tk()
window.title('CSP Fighter - Settings')
window.geometry("500x500")

def menu():
  window.destroy()
  os.system('python main.py')
def NOLAN():
	list = ["Unlocked"]
	pickle.dump(list, open("Settings.txt", "wb"))
back_bttn = Button(text='Back', command=menu)
back_bttn.place(x=5, y=5)

Nolan_bttn = Button(text='Sorry, we got lazy so there isnt actually anything worth your time in the settings menu', command=NOLAN)
Nolan_bttn.place(x=200,y=200)

window.mainloop()