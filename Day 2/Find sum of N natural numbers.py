n=int(input("Enter the number that you want sum:"))
b=(n*(n+1))/2
print("sum of",n,"is:",b)


#alternet methode 
n=int(input("Enter the number that you want sum:"))
a=0
for i in range(1,n+1):
    a=a+i
print("sum of",n,"is:",a)
