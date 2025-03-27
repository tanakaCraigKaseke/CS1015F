# Name: Craig Kaseke
# Student Number: KSKTAN003
# Date: 27-03-2025
# Last Modified: 27-03-2025
# Description: This script reads a list of space-separated numbers from the user
#              and removes duplicates while preserving the original order.
#              It does so without using any built-in functions like set().

# Prompt the user to enter a space-separated list of numbers
user_input = input("Enter an array of numbers (separated by spaces):\n")

# Convert the input into a list of integers
arr = [int(x) for x in user_input.split()]

# Create an empty list to store unique elements
unique_elements = []

# Loop through each element in the input list
for i in range(len(arr)):
    found = False  # Flag to track if duplicate is found

    # Check if the element already exists in unique_elements
    for j in range(len(unique_elements)):
        if arr[i] == unique_elements[j]:
            found = True
            break  # No need to continue if duplicate is found

    # If the element is not a duplicate, add it to unique_elements
    if not found:
        unique_elements.append(arr[i])

# Display the list with duplicates removed
print("Unique element array:", unique_elements)