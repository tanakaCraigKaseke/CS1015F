# Author: Craig Kaseke
# Student Number: KSKTAN003
# Date: 18-03-2025
# Last Modified: 18-03-2025
# Description: Script to test if a number is an Armstrong number.

def get_number():
    """Prompt user for an integer input and handle errors."""
    while True:
        try:
            return int(input('Enter a number:\n'))
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')
            exit(1)
        except EOFError:
            print("Invalid input. Please enter a valid integer.\n")
            exit(1)

def is_armstrong(num: int) -> bool:
    """Check if a number is an Armstrong number."""
    number_of_digits = len(str(num))
    total = sum(int(digit) ** number_of_digits for digit in str(num))
    return total == num

# Main program execution
test_number = get_number()

if is_armstrong(test_number):
    print(f'{test_number} is an Armstrong number.\n')
else:
    print(f'{test_number} is not an Armstrong number.\n')