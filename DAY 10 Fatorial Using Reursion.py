#DAY 10 : Factorial Using Reursion
#Problem: Write a funion to calculate the number by using fatorial over reursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  
print(factorial(0))  
