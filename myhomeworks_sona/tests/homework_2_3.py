# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
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


from lesson_2.homework_2_3 import result_1, result_2, result_3, result_4, result_5, result_6, result_7, result_8, \
    result_9, string_1, string_2, string_3, string_4, string_5, string_6, string_7
import pytest

def test_indexes_1():
    # Save to variable result_1 the first character of string_1 variable. In result_2 save the last character
    # of string_1. Use indexes.
    if result_1 == None or result_2 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert result_1 == string_1[0]
    assert result_2 == string_1[-1]


def test_indexes_2():
    # Save to variable result_3 string value from string_2 variable, written in reverse order, using concatenation.
    if result_3 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert result_3 == string_2[5] + string_2[4] + string_2[3] + string_2[2] + string_2[1] + string_2[0]


def test_slicing_1():
    # Slice string string_3 from 5th to 20th (excluding 20th) character and save the result to variable result_4
    if result_4 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert result_4 == string_3[5:20]


def test_slicing_2():
    # Slice string string_4 from 10th character to the end of the string. Save only every second character to variable
    # result_5
    if result_5 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert result_5 == string_4[10::2]


def test_slicing_3():
    # Slice string string_5 from the first to the last character, save only every forth character and
    # save the result to variable result_6
    if result_6 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert result_6 == string_5[::4]


def test_slicing_4():
    # Slice string string_6 from the first to 14th (including 14th) character, save only every third character and save
    # the result to variable result_7
    if result_7 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert result_7 == string_6[:15:3]

def test_slicing_5():
    # Save to variable result_8 string value from string_7 variable, written in reverse order, using slicing.
    if result_8 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert result_8 == string_7[::-1]


def test_range_1():
    # Create a range of numbers from 0 to 10 (excluding 10) and save it to result_9 variable
    if result_9 == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert result_9 == range(0,10)
