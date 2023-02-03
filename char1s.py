from tkinter import *
import pickle
import time
import sys
import os

filenext = "char2s"
filecurent = "char1"
window = Tk()
window.title('Player 1: Choose Character')
window.geometry("500x500")
c = Canvas(window, width=100, height=500)


#COMMANDS FOR BUTTON
def Return(): #Goes back to home screen
    os.system('python3 main.py')


#The following functions are used to create the buttons for selecting characters
def PLACEHOLDER(): 
    list = [
        "Placeholder",  #name
        "Fighter",
        "Slash",
        "Counter",
        "Heal"
    ]  #class
    #writes the list (^^^) to char1.txt for use later
    pickle.dump(list, open("txt/" + filecurent + ".txt", "wb"))
    window.destroy()
    os.system('python ' + filenext + '.py')


def NEVIL():
    list = [
        "Nevil",  #name
        "Ranged",
        "Gun",
        "Rocket Launcher",
        "Pistol Whip"
    ]  #class
    #writes the list (^^^) to char1.txt for use later
    pickle.dump(list, open("txt/" + filecurent + ".txt", "wb"))
    window.destroy()
    os.system('python ' + filenext + '.py')


def ELI():
    list = [
        "Eli",  #name
        "Fighter",
        "Slash",
        "Counter",
        "Heal"
    ]  #class
    #writes the list (^^^) to char1.txt for use later
    pickle.dump(list, open("txt/" + filecurent + ".txt", "wb"))
    window.destroy()
    os.system('python ' + filenext + '.py')


def DONALD():
    list = [
        "Donald",  #name
        "Tank",
        "Punch",
        "Headbutt",
        "Block"
    ]  #class
    #writes the list (^^^) to char1.txt for use later
    pickle.dump(list, open("txt/" + filecurent + ".txt", "wb"))
    window.destroy()
    os.system('python ' + filenext + '.py')


def DREW():
    list = [
        "Drew",  #name
        "Tank",
        "Punch",
        "Headbutt",
        "Block"
    ]  #class
    #writes the list (^^^) to char1.txt for use later
    pickle.dump(list, open("txt/" + filecurent + ".txt", "wb"))
    window.destroy()
    os.system('python ' + filenext + '.py')


def RHYS():
    list = ["Rhys", "Mage", "Fireball", "Stun", "Poison"]
    pickle.dump(list, open("txt/" + filecurent + ".txt", "wb"))
    window.destroy()
    os.system('python ' + filenext + '.py')


def JOEY():
    list = ["Joey", "Mage", "Fireball", "Stun", "Poison"]
    pickle.dump(list, open("txt/" + filecurent + ".txt", "wb"))
    window.destroy()
    os.system('python ' + filenext + '.py')


def GAVIN():
    list = [
        "Gavin",  #name
        "Ranged",
        "Gun",
        "Rocket Launcher",
        "Pistol Whip"
    ]  #class
    #writes the list (^^^) to char1.txt for use later
    pickle.dump(list, open("txt/" + filecurent + ".txt", "wb"))
    window.destroy()
    os.system('python ' + filenext + '.py')


#END COMMANDS

#END COMMANDS

#NORMAL BUTTON
back = Button(text="Back", command=Return)
back.place(x=10, y=10)
#END

#CLASS LABELS
c.create_text(35,
              75,
              text="Fighters:",
              fill="black",
              font=('Helvetica 10 bold'))
c.create_text(35,
              145,
              text="Rangers:",
              fill="black",
              font=('Helvetica 10 bold'))
c.create_text(35, 215, text="Tanks:", fill="black", font=('Helvetica 10 bold'))
c.create_text(35, 285, text="Mage:", fill="black", font=('Helvetica 10 bold'))
# IMAGE BUTTONS:

#Placeholdr Character
click_btn = PhotoImage(file='pics/icons/Placeholder.png')
button = Button(window,
                image=click_btn,
                command=PLACEHOLDER,
                height=50,
                width=50)

#Nevil Character
click_btn2 = PhotoImage(file='pics/icons/Nevil.png')
button2 = Button(window, image=click_btn2, command=NEVIL, height=50, width=50)

#Donald?
click_btn3 = PhotoImage(file='pics/icons/Donald.png')
button3 = Button(window, image=click_btn3, command=DONALD, height=50, width=50)

#gavin
click_btn4 = PhotoImage(file='pics/icons/Gavin.png')
button4 = Button(window, image=click_btn4, command=GAVIN, height=50, width=50)

#Rhys
click_btn5 = PhotoImage(file='pics/icons/Rhys.png')
button5 = Button(window, image=click_btn5, command=RHYS, height=50, width=50)

#Joey
click_btn6 = PhotoImage(file='pics/icons/Joey.png')
button6 = Button(window, image=click_btn6, command=JOEY, height=50, width=50)
#Eli
click_btn7 = PhotoImage(file='pics/icons/Eli.png')
button7 = Button(window, image=click_btn7, command=ELI, height=50, width=50)
#Drew
click_btn8 = PhotoImage(file='pics/icons/Drew.png')
button8 = Button(window, image=click_btn8, command=DREW, height=50, width=50)

# END IMAGE BUTTONS

#PACKS/PLACE AND MAINLOOP
c.place(x=0, y=0)
button.place(x=70, y=50)
button2.place(x=70, y=120)
button3.place(x=70, y=190)
button4.place(x=130, y=120)
button5.place(x=70, y=260)
button6.place(x=130, y=260)
button7.place(x=130, y=50)
button8.place(x=130, y=190)
window.mainloop()
#END
