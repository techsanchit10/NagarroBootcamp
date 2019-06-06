# 8. Explore the random module and create a number guessing game using it.
import random

print("\nRandom Roulette Game \nR = 2x \t G = 10x \t B = 2x")
print()
ch = 'y'
score = 1
mylist = ['R','B','G']

while(ch == 'y' or ch == 'Y'):
	choice = input("Enter a choice between R,B,G: \t")

	if choice == random.choice(mylist) and choice == 'R'  :
		score = 2*score
		print("\nCongratulations, Your score is doubled! \nScore= {}".format(score))
	elif choice == random.choice(mylist) and choice == 'B' :
		score = 2*score
		print("\nCongratulations, Your score is doubled! \nScore= {}".format(score))
	elif choice == random.choice(mylist) and choice == 'G' :
		score = 10*score
		print("\nCongratulations, Your score is increased by 10 times! \nScore= {}".format(score))
	else:
		print("\nBetter Luck next time\nScore= {}".format(score))

	ch = input("Do you want to play again?(y/n)")
