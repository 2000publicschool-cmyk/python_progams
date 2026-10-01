lst=[10, 25, 7, 89, 45]
length=len(lst)
total=sum(lst)
avr=total/length
print("average of all elements is",avr)





#other method
# Input list elements from user

list = list(map(int, input("Enter list elements separated by space: ").split()))
length=len(list)
total = sum(list)
avr=total/length
print("average of all elements is:", avr)

#other method
#without using sum function
total=0
lst=[10, 25, 7, 89, 45]
length=len(lst)
for i in lst:
    total+=i
avr=total/length
print("average of all elements is:", avr)
