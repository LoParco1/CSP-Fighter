import pygame, sys
from pygame.locals import QUIT
# import char1s
# import char2s
# import fight
# import stage_select

# pygame.init()
# DISPLAYSURF = pygame.display.set_mode((400, 300))
# pygame.display.set_caption('Hello World!')
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()

from tkinter import *
import pickle
import time
import sys
import os
Print = print()


def play():
	window.destroy()
	os.system('python char1s.py')
	#^^^a bit slower but works better

def quit():
	# yasure = Tk()
	# yasure.geometry("150x100")
	# yasure.configure(bg="black")
	# yasure.geometry("+500+500")
	# yasure.mainloop()
	window.destroy()
	
def options():
  pass


window = Tk()
window.title('CSP Fighter - Menu')
window.geometry("500x500")

#title in image
title= PhotoImage(file='Really Cool Logo.png')
img = Label(image=title)
img.pack()

#Buttons on home screen
play_bttn = Button(text = "Start Game", command=play)
play_bttn.pack()

Settings = Button(text = "Settings", command=options)#Brings up the settings menu 
Settings.pack()

terminate = Button(text="Quit", command=quit)
terminate.pack()



window.mainloop()