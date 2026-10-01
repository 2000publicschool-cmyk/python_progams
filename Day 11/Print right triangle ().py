print("1. Print right triangle default")
print("2. Print right triangle with user input")

choice=int(input("Enter your choice:"))
if choice==1:
    for i in range(1,6):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif choice==2:
    n=int(input("Enter the number of rows: "))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
        
