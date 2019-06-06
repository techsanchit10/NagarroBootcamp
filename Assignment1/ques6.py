# 6. Write a program to find second maximum number in a list.

def secondMax(l,n):
	min = l[0]
	for i in range(n):
		if l[i] < min:
			min = l[i]
			break
	print("2nd maximum number : {}".format(min))		

l = []
n=int(input("Enter size of list:"))
print("Enter {} list elements: ".format(n))
for i in range(n):
	k = int(input())
	l.append(k)
l.sort()
l.reverse()
print("List: {}".format(l))

secondMax(l,n)