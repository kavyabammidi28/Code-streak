def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return -1
    
    # Step 1: Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Step 2: Slide the window
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]  # add new element, remove old
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Example
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(arr, k))  # Output: 9  (subarray [5,1,3])
