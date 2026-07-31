# Program: Custom Exception Class with Logging

import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Custom Exception
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")

    print("Your age is:", age)

except InvalidAgeError as e:
    logging.error(e)

except ValueError:
    logging.error("Invalid input! Please enter a valid number.")