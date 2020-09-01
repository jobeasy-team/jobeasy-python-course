# You are given a list in list_1 variable, write a swap_first_last function to return a new list with
# the first and the last elements of the list swapped.
from typing import List, Any

list_1 = [1, 'asdasd', True, 2, False, 4, 'Hello world', None, range(1, 11), 100]


def swap_first_last(array_1):
    last = list_1.pop(-1)
    first = list_1.pop(0)
    list_1.append(first)
    list_1.insert(0, last)
    return list_1


# You are given a list in list_2 variable, write a reverse_list function which creates a new list in reversed order.
list_2 = [1, 'asdasd', True, 2, False, 4, 'Hello world', None, range(1, 11), 100]


def reverse_list(array_2):
    list_2.reverse()
    return list_2


# Create a list which contains only number items and save it to the list_3 variable. Then write multiply_list_items
# function to multiply all the items in a list.


list_3 = [1, 3, 4, 5, 0.8]


def multiply_list_items(array_3):
    result = 1
    for i in list_3:
        result *= i
    return result


# Create a list which contains only number items and save it to the list_4 variable. Then write a smallest_item_list
# function to get the smallest number from a list
list_4 = [10, 2, 5, 5, 0]


def smallest_item_list(array_4):
    """

    :type array_4: object
    """
    smallest = array_4[0]
    for item in array_4:
        if smallest < item:
            return smallest


# Given a list in list_5 variable, write a remove_duplicates_list function to remove duplicates from a list.
list_5 = [1, 2, 3, 1, 1, 1, 2, 3, 4, 'hello', 1, 2, 3, 4, 'hello', 'hello', 1]


def remove_duplicates_list(array_5):
    nodupel = []
    for item in array_5:
        if not item in nodupel:
            nodupel.append(item)
    return nodupel


'''
def remove_duplicates_list(array_5):
    nodupel = list(set(array_5))
    return nodupel
'''

# You are given a list in list_6 variable.Enter an integer number and save it to number_1 variable,
# write a longer_words_list function which will return the list of words that are longer than number_1
# from a given list of words.
number_1 = 5
list_6 = ['On', 'it', 'differed', 'repeated', 'wandered', 'required', 'in.', 'Then', 'girl', 'neat', 'why', 'yet',
          'knew', 'rose', 'spot.', 'Moreover', 'property', 'we', 'he', 'kindness', 'greatest', 'be', 'oh', 'striking',
          'laughter.', 'In', 'me', 'he', 'at', 'collecting', 'affronting', 'principles', 'apartments.', 'Has',
          'visitor',
          'law', 'attacks', 'pretend', 'you', 'calling', 'own', 'excited', 'painted.', 'Contented', 'attending',
          'smallness', 'it', 'oh', 'ye', 'unwilling.', 'Turned', 'favour', 'man', 'two', 'but', 'lovers.', 'Suffer',
          'should', 'if', 'waited', 'common', 'person', 'little', 'oh.', 'Improved', 'civility', 'graceful', 'few',
          'smallest', 'screened', 'settling.', 'Likely', 'active', 'her', 'warmly', 'has.']


def longer_words_list(array_6, number1):
    longer_words = []
    for item in array_6:
        if len(item) > number1:
            longer_words.append(item)
    return longer_words


# Given two lists in list_7 and list_8 variables. Write a function find_item_lists that takes two lists and returns
# True if they have at least one common member.


list_7 = [1, 2, 3, 1, 1, 1, 2, 3, 4, 'hello', 1, 2, 3, 4, 'hello', 'hello', 1]
list_8 = ['asdasd', True, 8, False, 94, 'Hello world', None, range(1, 11), 100, 1]


def find_item_lists(array_7, array_8):
    common = False
    for item7 in array_7:
        if item7 in array_8:
            common = True
    return common


# You are given a list in list_9 variable. Write a function string_to_list to convert a list of
# characters into a string.
list_9 = ['I', ' ', 'l', 'i', 'k', 'e', ' ', 'P', 'y', 't', 'h', 'o', 'n']


def list_to_string(list9):
    result = "".join(list9)
    return result


# Given a list of numbers in list_10 and a number number_2, write count_items_list function which will count number of
# occurrences of x in the given list
list_10 = [1, 2, 3, 1, 1, 1, 2, 3, 4]
number_2 = 3


def count_items_list(array_10, number2):
    count = 0
    for item in array_10:
        if item == number2:
            count += 1
    return count


# Given a list of numbers, write a function even_items_list to return new list which include all even numbers in
# given list.
list_11 = [1, 2, 3, 1, 1, 1, 2, 3, 4]


def even_items_list(array_11):
    evens = []
    for item in array_11:
        if item % 2 == 0:
            evens.append(item)
    return evens
