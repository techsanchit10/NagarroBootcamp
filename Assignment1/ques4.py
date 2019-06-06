# 4. Write a recursive function to print all possible strings of length k that can be formed from a set of n characters.


def printAllStrings(set, inStr, n, k): 
    if (k == 0) : 
        print(inStr) 
        return
  
    for i in range(n): 
        newStr = inStr + set[i] 
        printAllStrings(set, newStr, n, k - 1) 


set = []
inStr = ""
n=int(input("Enter no of set elements: "))
print("Enter {} set elements: ".format(n))

for i in range(n):
	s=input()
	set.append(s)

k=int(input("Length of each string: "))


printAllStrings(set,inStr,n,k)