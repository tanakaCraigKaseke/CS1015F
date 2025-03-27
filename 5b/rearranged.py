# Name: Craig Kaseke
# Student Number: KSKTAN003
# Date: 27-03-2025
# Last Modified: 27-03-2025
# Description: This script rearranges a sorted list of numbers such that the largest
#              number appears at index 0, the smallest at index 1, second largest at index 2,
#              and so on. It modifies the original list directly.


number_input = input("Enter sorted numbers separated by spaces:\n")
converted_to_array = [int(x) for x in number_input.split(" ")]
high_pointer = len(converted_to_array) - 1
low_pointer = 0
temp_array = []
take_high = True

while high_pointer >= low_pointer:
    if take_high:
        temp_array.append(converted_to_array[high_pointer])
        high_pointer -= 1
    else:
        temp_array.append(converted_to_array[low_pointer])
        low_pointer += 1
    take_high = not take_high

for i in range(len(converted_to_array)):
    converted_to_array[i] = temp_array[i]

print(f"Rearranged array: {converted_to_array}")

