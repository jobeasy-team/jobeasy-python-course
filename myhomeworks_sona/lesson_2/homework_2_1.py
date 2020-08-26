# Enter two numbers. If the first one is greater than the second, save first number in result_1,
# otherwise save the second number to the result_1 variable.

first_number = 22
second_number = 17

if first_number > second_number:
    result_1 = first_number
else:
    result_1 = second_number
print(result_1)


# Enter a random number in number_1 variable. If this number is 20 or
# higher save “Too high” text to result_2, otherwise save “Thank you”.
number_1 = 8
if number_1 >= 20:
    result_2 = 'too high'
else:
    result_2 = "thank you"
print(result_2)


# Enter your first name and last name in first_name and last_name variables. If the length of your first name is under
# five characters, join them together (without a space) and save it to result_3 variable in upper case. If the length
# of the first name is five or more characters, save their first name in lower case in result_3 variable.

first_name = "sona"
last_name = "vv"
if len(first_name) < 5:
    result_3 = first_name.upper() + last_name.upper()
else:
    result_3 = first_name.lower()
print(result_3)

# Enter a number between 10 and 20 (inclusive) and save number to number_2 variable
# If they enter a number within this range, save a message “Thank you” to result_4, otherwise a
# message “Incorrect answer” to result_4.

number_2 = 18
if 10 <= number_2 <= 20:
    result_4 = 'thank you'
else:
    result_4 = 'incorrect answer'
print(result_4)

# Enter your age. If you are 18 or over, save the message “You can vote” in result_5,
# if you are aged 17, save the message “You can learn to drive” in result_5 variable,
# if you are 16, save the message “You can buy a lottery ticket” in result_5,
# if you are under 16, save the message “You can go Trick-or-Treating” in result_5 variable.

age = 18
if age >= 17:
    result_5 = 'you can learn to drive'
elif age >= 18:
    result_5 = 'you can vote'
elif age == 16:
    result_5 = 'you can buy a lottery ticket'
else:
    result_5 = 'you can go trick or treat'
print(result_5)


# Enter a number between 1 and 12, save this value to month variable. Find which month is it.
# (January, February, March, April, May, June, Jule, August, September, October, November, December)
# Write answer in result_month in lower case

month = 6
result_month = 'none'
if month == 1:
    result_month = 'January'
elif month == 2:
    result_month = 'February'
elif month == 3:
    result_month = 'march'
elif month == 4:
    result_month = 'April'
elif month == 5:
    result_month = 'May'
elif month == 6:
    result_month = 'june'
elif month == 7:
    result_month = 'july'
elif month == 8:
    result_month = 'august'
elif month == 9:
    result_month = 'september'
elif month == 10:
    result_month = 'october'
elif month == 11:
    result_month = 'november'
elif month == 12:
    result_month = 'december'
result_month = result_month.lower()
print(result_month)
