def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Test cases
print(gcd(48, 18))   #6
print(gcd(100, 85))  # 5
print(gcd(7, 3))     # 1
