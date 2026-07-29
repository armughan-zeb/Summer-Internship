# Convert Celsius to Fahrenheit and vice versa
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

c = float(input("Enter temperature in Celsius: "))
print("Temperature in Fahrenheit =", celsius_to_fahrenheit(c))

f = float(input("Enter temperature in Fahrenheit: "))
print("Temperature in Celsius =", fahrenheit_to_celsius(f))

#Area Calculator

def area_circle(r):
    return 3.14 * r * r

def area_rectangle(length, width):
    return length * width

r = float(input("Enter radius of circle: "))
print("Area of Circle =", area_circle(r))

length = float(input("Enter length: "))
width = float(input("Enter width: "))
print("Area of Rectangle =", area_rectangle(length, width))