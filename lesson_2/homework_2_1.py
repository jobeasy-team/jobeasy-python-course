# Enter two numbers. If the first one is greater than the second, save first number in result_1,
# otherwise save the second number to the result_1 variable.
from random import random

first_number = 2
second_number = 8
if first_number > second_number:
    result_1 = first_number
else:
    result_1 = second_number
"""
input_1 = input ('Enter 1st number ')
first_number = int(input_1)
input_2 = input ('Enter 2nd number ')
second_number = int(input_2)
if first_number > second_number:
    result_1 = first_number
else:
    result_1 = second_number
    print(result_1)
"""
# Enter a random number in number_1 variable. If this number is 20 or
# higher save “Too high” text to result_2, otherwise save “Thank you”.

#number_1 = random.seed(50)
number_1 = 50
if number_1 >= 20:
    result_2 = 'Too high'
else:
    result_2 = 'Thank you'



# Enter your first name and last name in first_name and last_name variables. If the length of your first name is under
# five characters, join them together (without a space) and save it to result_3 variable in upper case. If the length
# of the first name is five or more characters, save their first name in lower case in result_3 variable.

first_name = 'James'
last_name = 'Bond'
if len(first_name) < 5:
    result_3 = (first_name+last_name).upper()
else:
    result_3 = first_name.lower()


# Enter a number between 10 and 20 (inclusive) and save number to number_2 variable
# If they enter a number within this range, save a message “Thank you” to result_4, otherwise a
# message “Incorrect answer” to result_4.

number_2 = 18
if 10 <= number_2 <= 20:
        result_4 = 'Thank you'
else:
    result_4 = 'Incorrect answer'



# Enter your age. If you are 18 or over, save the message “You can vote” in result_5,
# if you are aged 17, save the message “You can learn to drive” in result_5 variable,
# if you are 16, save the message “You can buy a lottery ticket” in result_5,
# if you are under 16, save the message “You can go Trick-or-Treating” in result_5 variable.

age = 100
if age >= 18:
    result_5 = 'You can vote'
elif age == 17:
    result_5 = 'You can learn to drive'
elif age == 16:
    result_5 = 'You can buy a lottery ticket'
else:
    result_5 = 'You can go Trick-or-Treating'

# Enter a number between 1 and 12, save this value to month variable. Find which month is it.
# (January, February, March, April, May, June, Jule, August, September, October, November, December)
# Write answer in result_month in lower case

month = 8
year = ['January', 'February', 'March', 'April', 'May', 'June', 'Jule', 'August', 'September', 'October', 'November', 'December']
result_month = (year[month - 1]).lower()
#print(result_month)
