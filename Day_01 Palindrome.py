# ✅ Day 01: Palindrome Check - Easy
# Problem: Check if a string is a palindrome

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# 🔍 Example Usage
if __name__ == "__main__":
    word = "madam"
    print("Word:", word)
    print("Is Palindrome:", is_palindrome(word))  # True
