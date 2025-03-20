# Author: Craig Kaseke
# Student Number: KSKTAN003
# Date: 18-03-2025
# Last Modified: 18-03-2025
# Description: The script accepts a starting number, n, and two
# additional inputs: the number of rows (r) and columns (c).
# It prints a grid of numbers, starting from n, with r rows and c columns.

def fetch_app_input():
    """
    Function to collect all user inputs in a single sequence.
    If any input is invalid, the entire process restarts.
    """
    while True:
        try:
            # Collect all inputs in a single attempt
            starting_num = int(input('Enter the starting number (n):\n'))
            num_of_rows = int(input('Enter the number of rows (r):\n'))
            num_of_columns = int(input('Enter the number of columns (c):\n'))

            # Validate that rows and columns are positive
            if starting_num > 0 and num_of_rows > 0 and num_of_columns > 0:
                return starting_num, num_of_rows, num_of_columns

            print('Rows and columns must be positive integers.')
        except ValueError:
            print('Invalid input. Please enter integers.')
        except EOFError:
            print('Invalid input. Please enter integers.')

# Get validated input values
starting_number, number_of_rows, number_of_columns = fetch_app_input()

# Initialize the starting number
current_number = starting_number

# Generate and print the grid
for _ in range(number_of_rows):
    for _ in range(number_of_columns):
        print(f"{current_number:3}", end=" ")  # Print formatted number with spacing
        current_number += 1  # Increment to the next number
    print()  # Move to the next line after each row
