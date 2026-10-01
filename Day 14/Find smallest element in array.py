lst=[10, 25, 7, 89, 45]
smallest=min(lst)
print("Smallest value is",smallest)





#other method
# Input list elements from user

list = list(map(int, input("Enter list elements separated by space: ").split()))

smallest = min(list)

print("Smallest element is:", smallest)
