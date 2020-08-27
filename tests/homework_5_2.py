# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
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


from lesson_5.homework_5_2 import counter, string_1, char_1, number_multiplication, number_1, number_reverse, number_2
import pytest


def test_counter():
    # Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
    # Write function counter, which will count how many times your character is included in your string
    if counter(string_1, char_1) == None or string_1 == None or char_1 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert string_1.count(char_1) == counter(string_1, char_1)


def test_number_multiplication():
    # Enter a random number and save it in variable number_1. Then create function number_multiplication which will
    # return a result of multiplication of digits this number.
    if number_multiplication(number_1) == None or number_1 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = 0
    num_string = str(number_1)
    length = len(num_string)
    index = 0
    while index < length:
        result *= num_string[index]
        index += 1
    assert number_multiplication(number_1) == result


def test_number_reverse():
    # Enter a random number and save it in variable number_2. Then create function number_reverse which will return
    # a number with digits of number_1 in reverse direction
    if number_reverse(number_2) == None or number_2 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    num_string = str(number_2)
    index = len(num_string)
    result = ''
    while index > 0:
        result += num_string[index]
        index -= 1
    assert number_multiplication(number_1) == int(result)

