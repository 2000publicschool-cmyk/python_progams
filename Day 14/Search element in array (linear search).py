lst=[10, 25, 7, 89, 45]
user=int(input("Enter the value that search:"))
if user in lst:
    print("Search result is found at",lst.index(user)+1)
else:
    print("Search result is not found")
