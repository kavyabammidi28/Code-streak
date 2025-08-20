# Reverse a string without using built-in functions
text = "Python"
reverse_text = ""

for char in text:
    reverse_text = char + reverse_text   # Add character at the front

print("Original String:", text)
print("Reversed String:", reverse_text)
