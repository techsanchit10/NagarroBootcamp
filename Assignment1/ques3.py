# 3. Write a python program to print this pattern:
#     For n = 5:
# 	```
# 			A
# 		   ABA
# 		  ABCBA
# 	     ABCDCBA
# 		ABCDEDCBA
# 	```

rows = int(input("Enter number of rows:"))
spaces = rows 
ch = 'A'
for i in range(rows+1):
	for j in range(spaces):
		print(' ', end =' ')

	for k in range(i-1):
		print(ch, end = ' ')
		ch = chr(ord(ch) + 1)

	for p in range(i,0,-1):
		print(ch, end = ' ')
		ch = chr(ord(ch) - 1)
	spaces -= 1
	ch = 'A'
	print()