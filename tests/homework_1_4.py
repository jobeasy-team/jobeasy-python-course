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
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT


# THIS FILE HAS ANSWERS. USE IT ONLY WHEN YOU HAVE SUCCESSFULLY PASSED HOMEWORK TESTS


from lesson_1.homework_1_4 import result_string_1, result_string_2, result_string_3, result_full_name, \
    first_name, last_name, result_full_name_length, result_ca_capital, result_planet
import pytest


def test_create_string():
    # Create three strings using three different methods. Save your result to result_string_1, result_string_2,
    # result_string_3 variables
    if result_string_1 == None or result_string_2 == None or result_string_3 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert type(result_string_1) is str
    assert type(result_string_2) is str
    assert type(result_string_3) is str


def test_create_full_name():
    # Enter your first and  last name. Join them together with a space in
    # between. Save a result in a variable result_full_name and
    # save the length of the whole name in result_full_name_length variable.
    if first_name == None or last_name == None or result_full_name == None or result_full_name_length == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert f'{first_name} {last_name}' == result_full_name
    assert type(result_full_name) is str
    assert len(f'{first_name} {last_name}') == result_full_name_length
    assert type(result_full_name_length) is int


def test_create_capital():
    # Enter the capital city of California State in lower case. Change the case to title case.
    # Save the result in result_ca_capital variable
    if result_ca_capital == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert f'sacramento'.title() == result_ca_capital


def test_result_planet():
    # Enter the name of our planet. Change the case to upper case. Save the result in
    # result_planet variable
    if result_planet == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert f'earth'.upper() == result_planet

