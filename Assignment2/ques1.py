# 1. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle. Also write functions to compare (<, >, <=, >=, ==, !=) 2 circles on the basis of their radius.

from math import *
from os import *

class Circle:
	def __init__(self,radius):
		self.radius = radius

	def area(self):
		self.area = pi * self.radius**2
		print("Area of circle with radius {} is : {}".format(self.radius,self.area))

	def perim(self):
		self.perim = 2 * pi * self.radius
		print("Perimeter of circle with radius {} is : {}".format(self.radius,self.perim))

	def __lt__(self,other):
		return self.radius < other.radius

	def __le__(self,other):
		return self.radius <= other.radius

	def __gt__(self,other):
		return self.radius > other.radius

	def __ge__(self,other):
		return self.radius >= other.radius

	def __eq__(self,other):
		return self.radius == other.radius

	def __ne__(self,other):
		return self.radius != other.radius

ch = 'y'
rad1 = int(input("Enter radius of 1st circle: "))
rad2 = int(input("Enter radius of 2nd cicle: "))

c1 = Circle(rad1)
c2 = Circle(rad2)


while(ch == 'y' or ch == 'Y'):
	system('cls')
	print("\n1. Area of Both Circles")
	print("\n2. Perimeter of Both Circles")
	print("\n3. Compare Radius of Both Circle")
	print()
	n = int(input("Enter a choice(1-3):"))
	if n == 1:
		c1.area()
		print()
		c2.area()

	elif n == 2:
		c1.perim()
		print()
		c2.perim()

	elif n == 3:
		if (c1 < c2):
			print("Radius of 1st cirlce is SMALLER than 2nd circle")
		if (c1 <= c2):
			print("Radius of 1st circle is SMALLER than or EQUAL to 2nd circle")
		if (c1 > c2):
			print("Radius of 1st circle is GREATER than 2nd circle")
		if (c1 >= c2):
			print("Radius of 1st circle is GREATER than or EQUAL to 2nd circle")
		if (c1 == c2):
			print("Radius of 1st circle is EQUAL to 2nd circle")
		if (c1 != c2):
			print("Radius of 1st circle is NOT EQUAL to 2nd circle")
	
	else:
		print()

	ch = input("Do you want to play again?(y/n)")

