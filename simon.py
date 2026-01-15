#!/usr/bin/python3
from random import randrange
import os, time

def showNumbers(list):
	for listNum in list:
		print(f"{listNum}", end="")
	print()

def clearTerminal():
	os.system('clear' if os.name == "posix" else "cls")

def checkResult(userInput, listNumbers):
	cmpListNumbers = ""
	for k in listNumbers:
		cmpListNumbers += str(k)

	for i in listNumbers:
		for j in userInput:
			if i == j:
				continue
			else:
				return False
	return True

list_numbers = []
status = True
correctAnswer = 0


for i in range(0,4):
	list_numbers.append(randrange(10))

while status:
	showNumbers(list_numbers)
	time.sleep(2)
	clearTerminal()
	userInput = input("Quelle est la liste de nombre ? : ")
	status = checkResult(userInput, list_numbers)
	print(status)
	if status:
		correctAnswer += 1
		list_numbers.append(randrange(10))
	else: 
		print(f"Vous avez perdu ! Votre score est de {correctAnswer}")