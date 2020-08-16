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


from lesson_2.homework_2_2 import number, number_1, number_2, result_1, result_2, result_3, result_4, first_name, \
    last_name, random_number
import pytest


def test_number():
    # Enter a number between 1 and 20, save this value to number variable.
    # If number is greater than 0 and less than or equal to 7, save the number * 10 to result_1.
    # If number is  greater than 7 and less than or equal to 15, save the result of floor division of the number divided by
    # 3 to result_1 variable
    # If number is  greater than 15 and less than or equal to 20, save the number raised to the power 3 to result_1
    # Else save the text "Wrong value" to result_1
    if number == None or result_1 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    if 0 < number <= 7:
        assert result_1 == number * 10
    elif 7 < number <= 15:
        assert result_1 == number // 3
    elif 15 < number <= 20:
        assert result_1 == number ** 3
    else:
        assert result_1 == "Wrong value"


def test_two_numbers():
    # Enter two numbers between 1 and 10, save this values to number_1 variable and number_2 variables.
    # If number_1 and number_2 are greater than 0 and less than or equal to 5 save in the product of their multiplication
    # to result_2
    # If one of the variables (number_1 or number_2) is greater than 5 and less than or equal to 10,
    # but the other isn't save the sum of the two numbers to result_2
    # If both numbers are greater than 5 and less than or equal to 10, multiply their sum by 3 and save it to result_2
    # Else save the text "Wrong values, try again" to result_2
    if number_1 == None or number_2 == None or result_2 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    if 0 < number_1 <= 5 and 0 < number_2 <= 5:
        assert result_2 == number_1 * number_2
    elif (0 < number_1 <= 5 and 5 < number_2 <= 10) or (0 < number_2 <= 5 and 5 < number_1 <= 10):
        assert result_2 == number_1 + number_2
    elif 5 < number_1 <= 10 and 5 < number_2 <= 10:
        assert result_2 == (number_1 + number_2) * 3
    else:
        assert result_2 == "Wrong values, try again"


def test_name_length():
    # Enter your first name and save it to first_name variable,
    # then Enter last name and save it to last_name
    # If first_name or last_name are shorter than 6 characters, save a full name (with a space between) to result_3
    # Else save first_name to result_3 as many times as length of last_name value
    if first_name == None or last_name == None or result_3 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    if len(first_name) < 6 or len(last_name) < 6:
        assert result_3 == f'{first_name} {last_name}'
    else:
        assert result_3 == first_name * len(last_name)


def test_even():
    # Enter a random number. Save this value to random_number variable
    # If this number is less 10 or greater than 99, save the text "Please, put in a number between 10 and 99" to result_4
    # If a number doesn't meet the first condition, find the remainder of random_value divided by 2.
    # If it is 0, save the text "Even number" to result_4 , else save the message "Odd number"
    if random_number == None or result_4 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    if random_number < 10 or random_number > 99:
        assert result_4 == "Please, put in a number between 10 and 99"
    else:
        if random_number % 2 == 0:
            assert result_4 == "Even number"
        else:
            assert result_4 == "Odd number"
