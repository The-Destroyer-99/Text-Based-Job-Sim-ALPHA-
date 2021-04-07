import pickle as pic
from os import system as sys
from time import sleep as slp
import random as rand

Gambits = int(0)

def s(a) :
	slp(a)

def clear() :
	sys("clear")

def StartUpLoadingBar() :
	s1 = rand.randint(1, 3)
	s2 = rand.randint(1, 3)
	s3 = rand.randint(1, 3)
	s4 = rand.randint(1, 3)
	s5 = rand.randint(1, 3)
	s6 = rand.randint(1, 3)
	s7 = rand.randint(1, 3)
	s8 = rand.randint(1, 3)
	s9 = rand.randint(1, 3)
	s10 = rand.randint(1, 3)
	
	print("Loading: ....................")
	slp(s1)
	sys("clear")
	print("Loading: ##..................")
	slp(s2)
	sys("clear")
	print("Loading: ###.................")
	slp(s3)
	sys("clear")
	print("Loading: ####................")
	slp(s4)
	sys("clear")
	print("Loading: #####...............")
	slp(s5)
	sys("clear")
	print("Loading: #######.............")
	slp(s6)
	sys("clear")
	print("Loading: #############.......")
	slp(s7)
	sys("clear")
	print("Loading: ################....")
	slp(s8)
	sys("clear")
	print("Loading: ##################..")
	slp(s9)
	sys("clear")
	print("Loading: ####################")
	slp(s10)
	sys("clear")

StartUpLoadingBar()

start_menu = input("""Hello!
1) Start New Game
2) Load Old Game

>> """)

sys("clear")
file_save_selection = -1
file_load_selection = -1
if start_menu == "1" :
	file_save_selection = input("""Pick File To Start With
1) Save 1
2) Save 2
3) Save 3
4) Save 4

>> """)
elif start_menu == "2" :
	file_load_selection = input("""
Pick File To Load

1) Save 1
2) Save 2
3) Save 3
4) Save 4
	
>>	""")
else :
	print("Invalid Input")

sys("clear")
if file_load_selection != -1:
  if file_load_selection == "1" :
    load_file = pic.load(open("save_1.dat", "rb"))
  elif file_load_selection == "2" :
    load_file = pic.load(open("save_2.dat", "rb"))
  elif file_load_selection == "3" :
    load_file = pic.load(open("save_3.dat", "rb"))
  elif file_load_selection == "4" :
    load_file = pic.load(open("save_4.dat", "rb"))
  else :
    print("Invalid Input")

if file_save_selection != -1:
  if file_save_selection == "1" :
    save_file = pic.dump( Gambits, open("save_1.dat", "wb"))
  elif file_save_selection == "2" :
    save_file = pic.dump( Gambits, open("save_2.dat", "wb"))
  elif file_save_selection == "3" :
    save_file = pic.dump( Gambits, open("save_3.dat", "wb"))
  elif file_save_selection == "4" :
    save_file = pic.dump( Gambits, open("save_4.dat", "wb"))
  else :
    print("Invalid Input")

sys("clear")

StartUpLoadingBar()

sys("clear")

if file_save_selection != 1 :
	print("Welcome Back!")
	clear()
	print(f"You Have {Gambits} Gambits!")
	clear()
	menu = input("""What Do You Want To Do?
	
1) Work
2) Shop (WIP)
3) Save
4) Backup Save
5) Save And Exit
6) Exit Without Saving (YOU WILL LOSE ALL UNSAVED PROGRESS)
""")
	if menu == "1" :
		rand_job_choice = rand.randint(1, 100)
		if rand_job_choice <= int(4) :
			print("You Shovled Shit Out Of A Public Toilet")
			Gambits = Gambits + 100
		elif rand_job_choice <= int(5) :
			print("You Got A Tour Of The_Destroyer_99's Dirty Ass House And You Desided To Clean It!")
			Gambits = Gambits + 100000
		elif rand_job_choice <= int(20) :
			print("You Yelled At A Manager For Not Wearing His Mask 2 Years AFTER 2021")
			Gambits = Gambits - 1000
		elif rand_job_choice <= int(40) :
			print("You Cleaned A Sink For Free!")
		elif rand_job_choice <= int(60) :
			print()
else :
	print("Welcome!!!")