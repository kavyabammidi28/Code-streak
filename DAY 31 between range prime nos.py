# ✅ Day 30: Find All Prime Numbers in a Range
# Problem:
# Write a program to print all prime numbers 
# between two numbers (inclusive).

def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

print(primes_in_range(10, 30))
