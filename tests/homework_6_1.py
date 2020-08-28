# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
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


from lesson_6.homework_6_1 import swap_first_last, reverse_list, multiply_list_items, smallest_item_list, \
    remove_duplicates_list, longer_words_list, find_item_lists, list_to_string, count_items_list, even_items_list, \
    list_1, list_2, list_3, list_4, list_5, number_1, list_6, list_7, list_8, list_9, number_2, list_10, list_11
import pytest


def test_swap_first_last():
    # You are given a list in list_1 variable, write a swap_first_last function to return a new list with
    # the first and the last elements of the list swapped.
    # Return this list

    if swap_first_last(list_1) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = list_1.copy()
    result[0], result[-1] = result[-1], result[0]
    assert swap_first_last(list_1) == result


def test_reverse_list():
    # You are given a list in list_2 variable, write a reverse_list function which creates a new list in reversed order.
    # Return this list
    if reverse_list(list_2) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = list_2.copy()
    result.reverse()
    assert reverse_list(list_1) == result


def test_multiply_list_items():
    # Create a list which contains only number items and save it to the list_3 variable. Then write multiply_list_items
    # function to multiply all the items in a list. Return result of multiplication
    if list_3 == None or multiply_list_items(list_3) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = 1
    for item in list_3:
        result *= item
    assert multiply_list_items(list_3) == result


def test_smallest_item_list():
    # Create a list which contains only number items and save it to the list_4 variable. Then write a smallest_item_list
    # function to get the smallest number from a list. Return smallest element
    if list_4 == None or smallest_item_list(list_4) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    min_1 = list_4[0]
    for item in list_4:
        if item < min_1:
            min_1 = item
    assert smallest_item_list(list_4) == min_1


def test_remove_duplicates_list():
    # Given a list in list_5 variable, write a remove_duplicates_list function to remove duplicates from a list.
    # Return new list without duplicates
    if remove_duplicates_list(list_5) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = []
    for item in list_5:
        if not item in result:
            result.append(item)
    assert remove_duplicates_list(list_5) == result


def test_longer_words_list():
    # You are given a list in list_6 variable.Enter an integer number and save it to number_1 variable,
    # write a longer_words_list function which will return the list of words that are longer than number_1
    # from a given list of words.
    if number_1 == None or longer_words_list(list_6, number_1) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = []
    for item in list_6:
        if len(item) > number_1:
            result.append(item)
    assert longer_words_list(list_6, number_1) == result


def test_find_item_lists():
    # Given two lists in list_7 and list_8 variables. Write a function find_item_lists that takes two lists and returns
    # True if they have at least one common member.


    if find_item_lists(list_7, list_8) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = False
    for item_1 in list_7:
        if item_1 in list_8:
            result = True
    assert find_item_lists(list_7, list_8) == result


def test_list_to_string():
    # You are given a list in list_9 variable. Write a function list_to_string to convert a list of
    # characters into a string.

    if list_to_string(list_9) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = ''.join(list_9)
    assert list_to_string(list_9) == result


def test_count_items_list():
    # Given a list of numbers in list_10 and a number number_2, write count_items_list function which will count number of
    # occurrences of number_2 in the given list

    if count_items_list(list_10, number_2) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = list_10.count(number_2)
    assert count_items_list(list_10, number_2) == result


def test_even_items_list():
    # Given a list of numbers, write a function even_items_list to return new list which include all even numbers in
    # given list.


    if even_items_list(list_11) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = []
    for item in list_11:
        if item % 2 == 0:
            result.append(item)
    assert even_items_list(list_11) == result
