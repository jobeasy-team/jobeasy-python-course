# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT


# THIS FILE HAS ANSWERS. USE IT ONLY WHEN YOU HAVE SUCCESSFULLY PASSED HOMEWORK TESTS


from lesson_2.homework_2_1 import first_number, second_number, result_1, number_1, result_2, first_name, last_name, \
    result_3, number_2, result_4, age, result_5, month, result_month
import pytest


def test_two_numbers():
    # Enter two numbers. If the first one is greater than the second, save first number in result_1,
    # otherwise save the second number to the result_1 variable.
    if first_number == None or second_number == None or result_1 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    if first_number > second_number:
        assert result_1 == first_number
    else:
        assert result_1 == second_number


def test_number():
    # Enter a number in number_1 variable. If this number is 20 or
    # # higher save “Too high” text to result_2, otherwise save “Thank you”.
    if result_2 == None or number_1 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    if number_1 >= 20:
        assert result_2 == "Too high"
    else:
        assert result_2 == "Thank you"


def test_full_name():
    # Enter your first name and last name in first_name and last_name variables. If the length of your first name is under
    # five characters, join them together (without a space) and save it to result_3 variable in upper case. If the length
    # of the first name is five or more characters, save their first name in lower case in result_3 variable.
    if first_name == None or last_name == None or result_3 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    if len(first_name) < 5:
        assert result_3 == f'{first_name}{last_name}'.upper()
    else:
        assert result_3 == f'{first_name}'.lower()


def test_number_between():
    # Enter a number between 10 and 20 (inclusive) and save number to number_2 variable
    # If they enter a number within this range, save a message “Thank you” to result_4, otherwise a
    # message “Incorrect answer” to result_4.
    if number_2 == None or result_4 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    if 10 <= number_2 <= 20:
        assert result_4 == f'Thank you'
    else:
        assert result_4 == f'Incorrect answer'


def test_ages():
    # Enter your age. If you are 18 or over, save the message “You can vote” in result_5,
    # if you are aged 17, save the message “You can learn to drive” in result_5 variable,
    # if you are 16, save the message “You can buy a lottery ticket” in result_5,
    # if you are under 16, save the message “You can go Trick-or-Treating” in result_5 variable.
    if age == None or result_5 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    if age < 16:
        assert result_5 == "You can go Trick-or-Treating"
    elif age < 17:
        assert result_5 == "You can buy a lottery ticket"
    elif age < 18:
        assert result_5 == "You can learn to drive"
    else:
        assert result_5 == "You can vote"


def test_month():
    # Enter a number between 1 and 12, save this value to month variable. Find which month is it.
    # (January, February, March, April, May, June, Jule, August, September, October, November, December)
    # Write answer in result_month in lower case
    if month == None or result_month == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    if month == 1:
        assert result_month == 'January'.lower()
    if month == 2:
        assert result_month == 'February'.lower()
    if month == 3:
        assert result_month == 'March'.lower()
    if month == 4:
        assert result_month == 'April'.lower()
    if month == 5:
        assert result_month == 'May'.lower()
    if month == 6:
        assert result_month == 'June'.lower()
    if month == 7:
        assert result_month == 'Jule'.lower()
    if month == 8:
        assert result_month == 'August'.lower()
    if month == 9:
        assert result_month == 'September'.lower()
    if month == 10:
        assert result_month == 'October'.lower()
    if month == 11:
        assert result_month == 'November'.lower()
    if month == 12:
        assert result_month == 'December'.lower()