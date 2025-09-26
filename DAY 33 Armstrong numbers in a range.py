# ✅ Day 33: Check Armstrong Numbers in a Range
# Problem:
# Write a program to find all Armstrong numbers between two numbers.

def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    return sum(int(d)**power for d in digits) == num

def armstrong_in_range(start, end):
    result = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            result.append(num)
    return result

print(armstrong_in_range(100, 500))

