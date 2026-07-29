#Program to Check Whether a Number is Prime or Not.

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")


#Program to check whether a string is palindrome or not.

string = input("Enter a string: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")