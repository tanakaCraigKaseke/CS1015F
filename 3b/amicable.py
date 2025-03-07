# Student number: KSKTAN003
# Student name: Craig Kaseke
# Date: 7 March 2025
# Last modified: 7 March 2025
# https://github.com/tanakaCraigKaseke/CS1015F.git
# program to determine weather two nummbers are amicable

first_number = int(input('Enter first number:\n'))
second_number = int(input('Enter second number:\n'))


# sigma first number
def sigma(n):
    positive_divisors_of_n = []

    for i in range(1, n):
        if n % i == 0:
            positive_divisors_of_n.append(i)

    return sum(positive_divisors_of_n)


if sigma(first_number) == second_number and sigma(second_number) == first_number:
    print(f'{first_number} and {second_number} are amicable numbers.')
else:
    print(f'{first_number} and {second_number} are not amicable numbers.')
