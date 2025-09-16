def number_pyramid(n):
    for i in range(1, n + 1):
        # Print spaces
        print(" " * (n - i), end="")
        # Print numbers
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Example usage
number_pyramid(5)
