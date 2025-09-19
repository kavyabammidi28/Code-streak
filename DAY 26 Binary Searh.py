def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
numbers = [10, 20, 30, 40, 50]
print(binary_search(numbers, 30))  # Output: 2
print(binary_search(numbers, 99))  # Output: -1
