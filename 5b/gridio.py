# Name: Craig Kaseke
# Student Number: KSKTAN003
# Date: 27-03-2025
# Last Modified: 27-03-2025
# Description: This script takes a 9x9 grid of digits from user input, then allows
#              the user to query values at specific (x, y) coordinates until -1 -1 is entered.

# Initialize an empty 2D list to store the 9x9 grid
grid = []

# Prompt user to enter 9 lines, each with 9 digits
print("Enter an array:")
for _ in range(9):
    # Read each line and convert each character to an integer
    row = [int(x) for x in input().strip()]
    grid.append(row)  # Add the row to the grid

# Enter loop to process coordinate queries
while True:
    # Prompt the user to input coordinates
    raw_coordinates = input("Enter coordinates:\n").strip()

    # Split input into two parts (x and y)
    x_y = raw_coordinates.split()

    # Validate that exactly two inputs were given
    if len(x_y) != 2:
        print("Invalid input. Please enter two numbers separated by a space.")
        continue

    # Convert coordinate strings to integers
    row_x = int(x_y[0])
    col_y = int(x_y[1])

    # Check for termination condition
    if row_x == -1 and col_y == -1:
        print('DONE')  # Optional message when exiting
        break

    # Validate that coordinates are within the valid grid range (0 to 8)
    if 0 <= row_x <= 8 and 0 <= col_y <= 8:
        # Access and print the value at the specified coordinates
        print("Value =", grid[row_x][col_y])
    else:
        # Handle invalid input outside the valid range
        print("Invalid coordinates. Please enter values between 0 and 8, or -1 -1 to exit.")