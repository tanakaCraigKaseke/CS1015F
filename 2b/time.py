# time.py
# Program to validate a given time
# Author: [Your Name]
# Date: [Current Date]

hours = int(input("Enter the hours:\n"))
minutes = int(input("Enter the minutes:\n"))
seconds = int(input("Enter the seconds:\n"))

if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
    print("Your time is valid.")
else:
    print("Your time is invalid.")