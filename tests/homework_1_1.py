# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
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


from lesson_1.homework_1_1 import a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, result_sum, result_diff, result_multiplication, \
    result_division, result_division_floored, result_division_remainder, result_power, result_negative
import pytest


def test_sum():
    # Sum up a and b. Save the expression to the result_sum variable
    if not result_sum:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert a + b == result_sum, f'Expected {a + b}, but got {result_sum}'


def test_diff():
    # Find the difference between c and d. Save the expression in the result_diff variable
    if not result_diff:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert c - d == result_diff, f'Expected {c - d}, but got {result_diff}'


def test_multiplication():
    # Multiply e by f. Save the expression to the result_multiplication variable
    if not result_multiplication:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert e * f == result_multiplication, f'Expected {e * f}, but got {result_multiplication}'


def test_division():
    # Divide g by h. Save the expression to the result_division variable
    if not result_division:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert g / h == result_division, f'Expected {g / h}, but got {result_division}'


def test_division_floored():
    # Do floor division for i and j. Save the expression to the result_division_floored variable
#<<<<<<< HEAD
    if not result_division_floored:
        pytest.skip (f"You didn't finish this task. the result variable equals None")
#=======
    if result_division_floored == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
#>>>>>>> upstream/master
    assert i // j == result_division_floored, f'Expected {i // j}, but got {result_division_floored}'


def test_division_remainder():
    # Calculate the remainder of k divided by l. Save expression to the result_division_remainder variable
    if not result_division_remainder:
        pytest.skip (f"You didn't finish this task. the result variable equals None")
    assert k % l == result_division_remainder, f'Expected {k % l}, but got {result_division_remainder}'


def test_power():
    # Rise m to the power n. Save the expression to the result_power variable
    if not result_power:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert m ** n == result_power, f'Expected {m ** n}, but got {result_power}'


def test_negative():
    # Convert an o variable to negative. Save the expression to the result_negative variable
    if not result_negative:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert -o == result_negative, f'Expected {-o}, but got {result_negative}'
