a=0
b=1
# user input
n=int(input("Enter the number of terms: "))
if n==1:
    print(a,end=" ")
if n==2:
    print(a,end=" ")
    print(b,end=" ")
else:
    print(a,end=" ")
    print(b,end=" ")
    for i in range(3,n+1):
        c=a+b
        print(c,end=" ") 
        a,b=b,c

        