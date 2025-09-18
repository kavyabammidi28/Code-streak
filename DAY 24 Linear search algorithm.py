def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

# Example usage
numbers = [10, 25, 30, 45, 50]
print(linear_search(numbers, 30))  # Output: 2
print(linear_search(numbers, 99))  # Output: -1
