# Input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Find smaller number
small = min(a, b)

for i in range(1, small + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

print("HCF is:", hcf)
