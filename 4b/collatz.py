# Author: Craig Kaseke
# Student Number: KSKTAN003
# Date: 18-03-2025
# Last Modified: 18-03-2025
# Description: a program called ‘collatz.py’ that accepts a positive integer and applies the rules to
# eventually reach 1. The program must gives an appropriate message when a negative integer or zero
# is entered or when any other input other than an integer is supplied.

# Command to zip: zip KSKTAN003.zip collatz.py armstrong.py

def get_number():
    while True:
       try:
           _number = int(input("Enter a positive integer:\n"))
           if _number <= 0:
               print("Please enter a positive integer.\n")
               exit(1)
           else:
            return  _number
       except ValueError:
           print("Invalid input. Please enter a valid integer.\n")
           exit(1)
       except EOFError:
           print("Invalid input. Please enter a valid integer.\n")
           exit(1)

def is_even() -> bool:
    return test_number % 2 == 0

test_number = get_number()

numbers_sequence = [test_number]
while test_number != 1:
    if is_even():
        even_number = test_number / 2
        numbers_sequence.append(even_number)
        test_number = even_number
    else:
        odd_number = 3 * test_number + 1
        numbers_sequence.append(odd_number)
        test_number = odd_number

number_string = ""
for number in numbers_sequence: number_string += str(int(number)) + " "

print(number_string)
