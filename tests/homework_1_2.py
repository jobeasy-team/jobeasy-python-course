# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
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


from lesson_1.homework_1_2 import a, b, c, d, e, f, result_1, result_2, result_3, result_4
import pytest


def test_power():
    # Find the second power of a variable. Save the expression to result_1 variable
    if not result_1:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert a ** 2 == result_1, f'Expected {a ** 2}, but got {result_1}'


def test_float():
    # Convert integer b to float. Save the expression to result_2 variable
    if not result_2:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert float(b) == result_2, f'Expected {float(b)}, but got {result_2}'


def test_int():
    # Convert a float variable c to integer. Save the expression to result_3 variable
    if not result_3:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert int(c) == result_3, f'Expected {int(c)}, but got {result_3}'


def test_int_math():
    # Sum up variables d and e and then multiply the total by f. Convert result to an integer and save the
    # expression to result_4 variable
    if not result_4:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert int((d + e) * f) == result_4
