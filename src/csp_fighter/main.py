"""Main module for the program."""

import os
import sys
import tkinter as tk  # it'll soon be unused, per pygame
from pathlib import Path
from tkinter import ttk

import pygame
from PIL import Image, ImageTk

# to prevent unintended side effects, put the bootstrapping in here

# if __name__ == "__main__":
#     pygame.init()  # init pygame
#     DISPLAYSURF = pygame.display.set_mode((400, 300))
#     pygame.display.set_caption("Hello World!")
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#         pygame.display.update()

# LEGACY CODE STARTS HERE
# To be converted


def play() -> None:
    """Make the game."""
    window.destroy()
    os.system("python3 char1s")  # Should this be hardcoded?
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


window = tk.Tk()
window.title("CSP Fighter - Menu")
window.geometry("500x500")


# title in image
# START ELI
p: Path = Path(os.path.realpath(__file__)).parent
logo_file: Path = Path.resolve(p / "pics" / "really_cool_logo.png")
pil_img: Image = Image.open(logo_file)  # modifications can be made using this
mod_img: Image = pil_img  # you can modify the image here
title_img = ImageTk.PhotoImage(mod_img)

# END ELI

img = ttk.Label(image=title_img)
img.pack()

# Buttons on home screen
play_btn = ttk.Button(text="Start Game", command=play)
play_btn.pack()

Settings = ttk.Button(text="Settings", command=options)  # Brings up the settings menu
Settings.pack()

terminate = ttk.Button(text="Quit", command=quit_game)
terminate.pack()


window.mainloop()
