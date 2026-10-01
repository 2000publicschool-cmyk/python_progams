
a=1
for i in range(6,1,-1):
    for j in range(7,i,-1):
        print(" ",end='')
    for k in range(1,i):
        print(a,end=" ")
        a=a+1
        if a==16:
            break
    print()


