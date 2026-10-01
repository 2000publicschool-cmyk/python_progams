lst=[10, 25, 7, 89, 45]
total=sum(lst)
print("sum of all elements is",total)





#other method
# Input list elements from user

list = list(map(int, input("Enter list elements separated by space: ").split()))

total = sum(list)

print("sum of all elements is:", total)

#other method
#without using sum function
total=0
lst=[10, 25, 7, 89, 45]
for i in lst:
    total+=i
print("sum of all elements is:", total)
