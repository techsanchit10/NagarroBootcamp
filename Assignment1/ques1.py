# 1. Given an integer n, print a nXn matrix with squares (outermost to innermost) having values n, then n-1 and so on.
# 	For example, given 5, output is:
# 	```
# 	5 5 5 5 5
# 	5 4 4 4 5
# 	5 4 3 4 5
# 	5 4 4 4 5 
# 	5 5 5 5 5
# 	```

def pattern(n):
	if n%1 == 0:
		for i in range(n):
			for j in range(n):
				print (max(n-i,i+1,j+1,n-j), end = '\t')

			print("\n")
	else:
		print("n should be whole number!")

n = int(input("Enter size of matrix: "))
pattern(n)
