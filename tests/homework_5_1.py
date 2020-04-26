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


from lesson_5.homework_5_1 import print_name_three_times, name_1, print_name_number_times, number_1, name_2, sum_digits,\
    string_number_1, sum_even_numbers
import pytest


def test_print_name_three_times():
    # Enter your name, save it in name variable and create function print_name_three_times which returns
    # value that is equal to your name three times
    if print_name_three_times(name_1) == None or name_1 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert name_1 * 3 == print_name_three_times(name_1)


def test_print_name_number_times():
    # Modify your previous program so that it will enter your name (save it in variable  name_2) and a number
    # (save in variable number) and then display their name that number of times. Each time add your name to result
    # variable
    if print_name_number_times(number_1, name_2) == None or name_2 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert name_2 * number_1 == print_name_number_times(number_1, name_2)


def test_sum_digits():
    # Enter a random string, which includes only digits. Write function sum_digits which find a sum of digits in this
    # string
    result = 0
    if sum_digits(string_number_1) == None or string_number_1 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    for char in string_number_1:
        result += int(char)
    assert result == sum_digits(string_number_1)




# Create function which sums up all even numbers between 2 and 100 (include 100)
def test_sum_even_numbers():
    if sum_even_numbers() == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = 0
    for number in range(2, 101, 2):
        result += number
    assert result == sum_even_numbers()


