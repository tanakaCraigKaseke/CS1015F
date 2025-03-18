# bmi_calculator.py
# Program to calculate BMI and determine category
# Author: [Your Name]
# Date: [Current Date]

weight = float(input("Enter your weight in kg:\n"))
height = float(input("Enter your height in meters:\n"))

bmi = weight / (height ** 2)

print(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 25:
    print("Category: Normal weight")
elif 25 <= bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")