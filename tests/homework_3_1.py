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


from lesson_3.homework_3_1 import result_1, name_1, result_2, number_1, name_2, result_3,\
    string_number_1, result_4
import pytest


def test_print_name_three_times():
    # Enter your name, save it in name variable and save in result_1 variable your name repeated 3 times (use loops)
    if result_1 == None or name_1 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert name_1 * 3 == result_1


def test_print_name_number_times():
    # Modify your previous program so that it will enter your name (save it in variable  name_2) and a number
    # (save in variable number) and then save in result_2 variable your name repeated as many times as number_1 is
    # (use loops)
    if result_2 == None or name_2 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert name_2 * number_1 == result_2


def test_sum_digits():
    # Enter a random string, which includes only digits. Write code which find a sum of digits in this string and save it
    # into result_3 variable
    result = 0
    if result_3 == None or string_number_1 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    for char in string_number_1:
        result += int(char)
    assert result == result_3




# Create code which sums up all even numbers between 2 and 100 (include 100) and save it in result_4 variable
def test_sum_even_numbers():
    if result_4 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = 0
    for number in range(2, 101, 2):
        result += number
    assert result == result_4


