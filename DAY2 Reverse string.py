def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Example usage
input_string = "hello"
print("Original:", input_string)
print("Reversed:", reverse_string(input_string))
   

#output:
Original: hello
Reversed: olleh