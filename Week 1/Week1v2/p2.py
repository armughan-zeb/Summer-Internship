# Program: Check if Two Strings are Anagrams

# Take input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Remove spaces and convert to lowercase
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

# Check if the sorted strings are equal
if sorted(string1) == sorted(string2):
    print("The strings are Anagrams.")
else:
    print("The strings are Not Anagrams.")
    