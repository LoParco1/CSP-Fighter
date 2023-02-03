from tkinter import *
import pickle
import time
import sys
import os
import random
from fight2 import hpupdate
current_turn = pickle.load(open("turn.txt","rb"))
def end_game():
	os.system('Python main.py')
	w.destroy()
def attack1():
	global current_turn
	if current_turn == 1 or current_turn == 3:

		if hp[0] <= 0:
			end_game()
		else:
			print(hp[0])
	else:
		if hp[1] <= 0:
			end_game()
		else:
			print(hp[1])
		
	if current_turn == 1:
		if p1[2] == "Slash":
				health = [hp[0] - random.randint(10,20), hp[1]]
				pickle.dump(health, open("txt/health.txt", "wb"))
				print("slash")
		elif p1[2] =="Gun":
			health = [hp[0] - random.randint(10,20), hp[1]]
			pickle.dump(health, open("txt/health.txt", "wb"))
			print("gun")
		elif p1[2] == "Punch":
			health = [hp[0] - random.randint(10,20), hp[1]]
			pickle.dump(health, open("txt/health.txt", "wb"))
			print("punch")
		elif p1[2] == "Fireball":
			health = [hp[0] - random.randint(10,20), hp[1]]
			pickle.dump(health, open("txt/health.txt", "wb"))
			print("Fireball")
		current_turn += 1
		print(current_turn)


	elif current_turn == 2:
		if p2[2] == "Slash":
				health = [hp[0], hp[1]-random.randint(10,20)]
				pickle.dump(health, open("txt/health.txt", "wb"))
				print("slash")
		elif p2[2] =="Gun":
			health = [hp[0] - random.randint(10,20), hp[1]]
			pickle.dump(health, open("txt/health.txt", "wb"))
			print("gun")
		elif p2[2] == "Punch":
			health = [hp[0] - random.randint(10,20), hp[1]]
			pickle.dump(health, open("txt/health.txt", "wb"))
			print("punch")
		elif p2[2] == "Fireball":
			health = [hp[0] - random.randint(10,20), hp[1]]
			pickle.dump(health, open("txt/health.txt", "wb"))
			print("Fireball")
		current_turn +=1
		print(current_turn)

	elif current_turn == 3:
		if p12[2] == "Slash":
				health = [hp[0] - random.randint(10,20), hp[1]]
				pickle.dump(health, open("txt/health.txt", "wb"))
				print("slash")
		elif p12[2] =="Gun":
			health = [hp[0] - random.randint(10,20), hp[1]]
			pickle.dump(health, open("txt/health.txt", "wb"))
			print("gun")
		elif p12[2] == "punch":
			health = [hp[0] - random.randint(10,20), hp[1]]
			pickle.dump(health, open("txt/health.txt", "wb"))
			print("punch")
		elif p12[2] == "Fireball":
			health = [hp[0] - random.randint(10,20), hp[1]]
			pickle.dump(health, open("txt/health.txt", "wb"))
			print("Fireball")
		current_turn += 1
		print(current_turn)
		
	elif current_turn == 4:
		if p22[2] == "Slash":
				health = [hp[0], hp[1]- random.randint(10,20)]
				pickle.dump(health, open("txt/health.txt", "wb"))
				print("slash")
		elif p22[2] =="Gun":
			health = [hp[0] - random.randint(10,20), hp[1]]
			pickle.dump(health, open("txt/health.txt", "wb"))
			print("gun")
		elif p22[2] == "Punch":
			health = [hp[0] - random.randint(10,20), hp[1]]
			pickle.dump(health, open("txt/health.txt", "wb"))
			print("punch")
		elif p22[2] == "Fireball":
			health = [hp[0] - random.randint(10,20), hp[1]]
			pickle.dump(health, open("txt/health.txt", "wb"))
			print("Fireball")
		current_turn =1
		print(current_turn)
	pickle.dump(current_turn,open("turn.txt", "wb"))
	os.system('python3 moves.py')
	w.destroy()



w = Tk()

w.geometry("200x500")
hp = pickle.load(open("txt/health.txt", "rb"))
p1 = pickle.load(open("txt/char1.txt", "rb"))
p2 = pickle.load(open("txt/char2.txt", "rb"))
p12 = pickle.load(open("txt/char12.txt", "rb"))
p22 = pickle.load(open("txt/char22.txt", "rb"))

if current_turn == 1:
	w.title('Player1')
	button1 = Button(w, text=p1[2], command=attack1)
elif current_turn == 2:
	w.title('Player2')
	button1 = Button(w, text=p2[2], command = attack1)
elif current_turn == 3:
	w.title('Player1')
	button1 = Button(w, text=p12[2], command = attack1)
elif current_turn == 4:
	w.title('Player2')
	button1 = Button(w, text=p22[2], command = attack1)
	
button1.place(x=0, y=0)
w.mainloop()