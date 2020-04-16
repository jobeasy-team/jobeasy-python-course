# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
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


from lesson_2.homework_2_2 import result_string_1, result_string_2, result_value, number, result_string_3, n, word
import pytest


def test_newline_string():
    # Change result_string_1 that 'very simple language' will be displayed on a new line
    if result_string_1 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert 'Python is the\nvery simple language' or 'Python is the \nvery simple language' or \
           'Python is the \n very simple language' == result_string_1


def test_fix_string():
    # Change result_string_2 to print out the phrase: 'What does the word 'integer' mean'
    if result_string_2 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert 'What does the word \'integer\' mean' == result_string_2


def test_input_value():
    # Assign number variable to value "5" (as a string). Then rise the number to the power 3.
    # Save the expression to result_value variable
    if number == None or result_value == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert result_value == int(number) ** 3


def test_multiplication_string():
    # Enter a random number, then save the value to n variable.
    # Finally, you should repeat the variable "word" n times and save the value to result_string_3
    if n == None or result_string_3 == None or word == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert n * word == result_string_3
