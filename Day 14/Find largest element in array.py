lst=[10, 25, 7, 89, 45]
largest=max(lst)
print("Largest value is",largest)





#other method
# Input list elements from user

list = list(map(int, input("Enter list elements separated by space: ").split()))

largest = max(list)

print("Largest element is:", largest)
