# Day 20: Multiplication Table

n = int(input("Enter a number: "))

print(f"\nMultiplication Table of {n}:\n")
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
