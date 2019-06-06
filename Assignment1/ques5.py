import json

class Student:

	def __init__(self, roll, name, branch):
		self.roll = roll
		self.name = name
		self.branch = branch


s = int(input("Enter number of Students: "))
Stud = []

for i in range(s):
	print("\nDetails of {}th Student: ".format(i+1))
	roll = int(input("Enter roll-no: "))
	name = input("Enter name: ")
	branch = input("Enter Branch: ")

	Stud.append(Student(roll,name,branch))

l = []
for i in range(s):
	l.append(Stud[i].__dict__)

print(json.dumps(l, indent = 2))
