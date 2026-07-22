#Using Loops

n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


#Using Recursion

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the number of terms: "))

for i in range(n):
    print(fibonacci(i), end=" ")