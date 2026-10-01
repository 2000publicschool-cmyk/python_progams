lst=[10, 25, 7, 89, 45]
even=0
odd=0
for i in lst:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Even number is list is",even)
print("Odd number is list is",odd)


#other method
lst = [10, 25, 7, 89, 45]
even = []
odd = []
for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers are:", even)
print("Odd numbers are:", odd)

print("Count of even numbers:", len(even))
print("Count of odd numbers:", len(odd))
