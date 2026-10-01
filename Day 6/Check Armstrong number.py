a=input("Enter the number:")
l=len(a)
b=0
for i in range(0,l):
    b=b+int(a[i])**l
c=str(b)
if a==c:
    print(a,"is armstrong number")
else:
    print(a,"is not armstrong number")
    
