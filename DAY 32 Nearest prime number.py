#✅ DAY -32 Nearest Prime Numbers

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def nearest_primes(n):
    if is_prime(n):
        return [n]
    
    lower, upper = n - 1, n + 1
    while True:
        if lower > 1 and is_prime(lower) and is_prime(upper):
            return [upper, lower]   # both equally near
        if lower > 1 and is_prime(lower):
            return [lower]
        if is_prime(upper):
            return [upper]
        lower -= 1
        upper += 1

# Example usage
print(nearest_primes(10))  # [11, 7]
print(nearest_primes(17))  # [17]
print(nearest_primes(20))  # [19]
