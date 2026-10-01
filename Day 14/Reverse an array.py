lst=[10, 25, 7, 89, 45]
print("Old list is",lst)

print("reverse list is",lst[::-1])


lst = [10, 25, 7, 89, 45]
print("Old list is:", lst)
rev = []
for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])
print("Reverse list is:", rev)

