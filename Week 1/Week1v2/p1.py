# Program: Reverse a String Without Using a Built-in Reverse Function

# Take input from the user
string = input("Enter a string: ")

# Initialize an empty string
reverse = ""

# Reverse the string using a loop
for char in string:
    reverse = char + reverse

# Display the reversed string
print("Reversed String:", reverse)