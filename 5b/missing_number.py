# Name: Craig Kaseke
# Student Number: KSKTAN003
# Date: 27-03-2025
# Last Modified: 27-03-2025
# Description: This script takes a space-separated list of integers as input,
#              identifies a missing number in the sequence based on the
#              expected sum between the minimum and maximum values, and prints
#              the missing number if one exists, or a message if the sequence is complete.

# Prompt the user for input
number_input = input("Enter an array of numbers (separated by spaces):\n")

# Split the string into a list of strings, then convert each to an integer
array = [int(x) for x in number_input.split()]

# Calculate the actual sum of the numbers entered
actual_sum = sum(array)

# Determine the expected sum using the range from min to max
expected_sum = sum(range(min(array), max(array) + 1))

# Compare sums to check if a number is missing
if actual_sum == expected_sum:
    print("There is no missing number.")
else:
    # The missing number is the difference between expected and actual
    print(f"Missing number: {expected_sum - actual_sum}")