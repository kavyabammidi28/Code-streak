# ✅ Day 05: Count vowels in a string
# Problem: Write a Python function that counts the number of vowels in a string.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello world"))  # Output: 3
