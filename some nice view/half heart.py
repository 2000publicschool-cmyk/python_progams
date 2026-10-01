for row in range(6):
    for coloum in range(4):
        if ((row==0 and coloum%3!=0)or
            (row==1 and coloum%3==0)or
            (row==2 and coloum%3==0)or
            (row==3 and coloum%2!=0)or
            (row==4 and coloum ==3 or coloum== 4)or
            (row - coloum==2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
        


