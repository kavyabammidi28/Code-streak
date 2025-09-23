def diamond_pattern(n):
    # Upper half
    for i in range(1, n+1, 2):
        print(" " * ((n - i) // 2) + "*" * i)
    # Lower half
    for i in range(n-2, 0, -2):
        print(" " * ((n - i) // 2) + "*" * i)

# Example usage
diamond_pattern(5)
