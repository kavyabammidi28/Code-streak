#✅ Day 9: Palindrome Checker
#Problem:
#Write a Python function that checks if a given string is a palindrome
#(reads the same backward as forward). Ignore spaces and case sensitivity.

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(is_palindrome("Race car"))   
print(is_palindrome("Python"))     
