def fibonacci_iter(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

num = int(input("\nEnter number of terms: "))
print("Fibonacci Series (loop):")
fibonacci_iter(num)
