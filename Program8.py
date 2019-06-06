# 8. Explore the random module and create a number guessing game using it.


import random

def generateRandomNumber():
	randomNumber=random.randint(1,100)
	return randomNumber



def askUserForNumber(message = "Guess the Number : "):
	userNumber=int(input(message))
	return userNumber


def checkUserNumber(userNumber,randomNumber):
	if userNumber > randomNumber:
		return "Number is Too High"
	elif userNumber < randomNumber:
		return "Number is Too Low"
	elif userNumber == randomNumber:
		return "Congratulation, you  found a number"

def main():
	randomNumber = generateRandomNumber()
	userNumber = askUserForNumber()
	message	= checkUserNumber(userNumber,randomNumber)

	while message != "Congratulation, you found a number" :
		print(message)
		userNumber = askUserForNumber("Try Again") 

main()