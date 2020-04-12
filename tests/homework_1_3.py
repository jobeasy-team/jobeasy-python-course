# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
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


from lesson_1.homework_1_3 import a, result_1, result_2, result_3
import math
import pytest


def test_rounding():
    # Round a off to three decimal places.
    if not result_1:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert round(a, 3) == result_1, f'Expected {round(a, 3)}, but got {result_1}'


def test_rounding_greater():
    # Round up result_2 to greater value.
    if not result_2:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert math.ceil(5 / 2 * 6 + 1.25 - 4) == result_2, f'Expected {math.ceil(5 / 2 * 6 + 1.25 - 4)}, ' \
                                                        f'but got {result_2}'


def test_rounding_less():
    # Round up result_3 to lesser value.
    if not result_3:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert math.floor(8 / 3 * 5 + 4.75 - 7) == result_3, f'Expected {math.floor(8 / 3 * 5 + 4.75 - 7)},' \
                                                         f' but got {result_3}'
