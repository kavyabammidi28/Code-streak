# Problem: Write a function to find the largest number in a list without using the built-in max() function.

def find_max(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([4, 10, 2, 89, 33]))
