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
	listUserInput = []
	for i in userInput:
		listUserInput.append(int(i))

	for j in range(0, len(listNumbers)):
		if listNumbers[j] == listUserInput[j]:
			result = True
		else:
			result = False
	return result

def checkError(input):
	listUserInput = []
	for i in input:
		listUserInput.append(i)

	for j in range(0, len(listUserInput)):
		if listUserInput[j] >= '0' and listUserInput[j] <= '9':
			result = True
		else:
			return False
	return result

def difficult(difficulty):
	match difficulty:
		case "easy":
			return [5, 1]
		case "medium":
			return [3, 2]
		case "hard":
			return [2, 4]
		case "impossible":
			return [1, 10]

list_numbers = []
status = True
correctAnswer = 0

for i in range(0,4):
	list_numbers.append(randrange(10))

userInputDifficulty = input("Quel difficulté voulez vous choisir ? (easy, medium, hard, impossible) : ")

while status:
	listValueDifficulty = difficult(userInputDifficulty)
	print(listValueDifficulty)
	showNumbers(list_numbers)
	time.sleep(listValueDifficulty[0])
	clearTerminal()
	userInput = input("Quelle est la liste de nombre ? : ")
	error = checkError(userInput)
	if error == True:
		if len(userInput) == len(list_numbers):
			status = checkResult(userInput, list_numbers)
			if status:
				correctAnswer += 1
				for i in range(0, listValueDifficulty[1]):
					list_numbers.append(randrange(10))
			else: 
				print(f"Vous avez perdu ! Votre score est de {correctAnswer} !")
		else:
			print("La taille de saisie n'est pas correct !")
	else: 
		print("La saisie contient des caractères autres que des chiffres !")
		