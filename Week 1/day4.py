# Convert Celsius to Fahrenheit and vice versa
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

c = float(input("Enter temperature in Celsius: "))
print("Temperature in Fahrenheit =", celsius_to_fahrenheit(c))

f = float(input("Enter temperature in Fahrenheit: "))
print("Temperature in Celsius =", fahrenheit_to_celsius(f))