# 2. Write a python program to print this pattern:
#     For n = 5:
#     ```
#         *
#        ***
#       *****
#      *******
#     *********
#     ```


rows = int(input("Enter number of rows"))
spaces = rows 
for i in range(rows+1):
    for j in range(spaces):
        print(' ',end=' ')
    for k in range(2*i - 1):
    	print("*", end = " ")
    spaces -= 1

    print("\n")