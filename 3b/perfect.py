# Student number: KSKTAN003
# Student name: Craig Kaseke
# Date: 7 March 2025
# Last modified: 7 March 2025
# program description: program called ‘perfect.py’ determines if a given number is a perfect number or not.

number_input = int(input('Enter a number:\n'))
# proper divisors
proper_divisors = []
for i in range(1, number_input ):
    if number_input % i == 0:
        proper_divisors.append(i)

print(f'The proper divisors of {number_input} are:\n',*proper_divisors,'\n')

is_perfect = sum(proper_divisors) == number_input

if is_perfect:
    print(f'{number_input} is a perfect number.\n')
else:
    print(f'{number_input} is not a perfect number.\n')