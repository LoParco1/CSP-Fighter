"""Main module for the program."""

import os
import pickle
import sys
import time
from pathlib import Path
from tkinter import *  # 2 things - 1) wildcard imports are bad, and 2) it'll soon be unused

import pygame
from pygame.locals import QUIT

# to prevent unintended side effects, put the bootstrapping in here
if __name__ == "__main__":
    pygame.init()  # init pygame
    DISPLAYSURF = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Hello World!")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

# LEGACY CODE STARTS HERE
# To be converted


def play() -> None:
    """Setup the game."""
    window.destroy()
    os.system("python char1s.py")  # Should this be hardcoded?
    # ^^^a bit slower but works better


def quit_game() -> None:
    """End the game."""
    # yasure = Tk()
    # yasure.geometry("150x100")
    # yasure.configure(bg="black")
    # yasure.geometry("+500+500")
    # yasure.mainloop()
    window.destroy()


def options() -> None:
    """Set the options."""
    pass


window = Tk()
window.title("CSP Fighter - Menu")
window.geometry("500x500")

# title in image
title = PhotoImage(file="pics/really_cool_logo.png")
img = Label(image=title)
img.pack()

# Buttons on home screen
play_bttn = Button(text="Start Game", command=play)
play_bttn.pack()

Settings = Button(text="Settings", command=options)  # Brings up the settings menu
Settings.pack()

terminate = Button(text="Quit", command=quit_game)
terminate.pack()


window.mainloop()
