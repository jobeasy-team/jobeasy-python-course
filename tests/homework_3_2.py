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


from lesson_3.homework_3_2 import result_1, string_1, char_1, result_2, number_1, result_3, number_2
import pytest


def test_counter():
    # Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
    # Write code, which will count how many times your character is included in your string.
    # Save result to result_1 variable
    if result_1 == None or string_1 == None or char_1 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert string_1.count(char_1) == result_1


def test_number_multiplication():
    # Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
    # and save result in the result_2 variable.
    if result_2 == None or number_1 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = 0
    num_string = str(number_1)
    length = len(num_string)
    index = 0
    while index < length:
        result *= int(num_string[index])
        index += 1
    assert result_2 == result


def test_number_reverse():
    # Enter a random number and save it in variable number_2. Then create code which will return
    # a number with digits of number_1 in reverse order. Save it in result_3 variable
    if result_3 == None or number_2 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    num_string = str(number_2)
    index = len(num_string)
    result = ''
    while index > 0:
        result += num_string[index-1]
        index -= 1
    assert result_3 == int(result)

