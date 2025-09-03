def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    return num == total

# User input
n = int(input("Enter a number: "))

if is_armstrong(n):
    print(n, "is an Armstrong number")
else:
    print(n, "is NOT an Armstrong number")
