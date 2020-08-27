# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
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


from lesson_6.homework_6_2 import countries, your_choice_country, your_choice_number, find_index_by_value, \
    find_value_by_index, new_team_name, new_team_city, nhl_hockey_teams, add_your_own_team, dict_1, dict_2, \
    join_dicts, number_1, create_numbers_dict, dict_3, sum_up_hockey_cups, dict_4, remove_item_by_key, dict_5, \
    find_min_max, dict_6, remove_duplicates

import pytest


def test_find_index_by_value():
    # Enter a country and save it to variable your_choice_country. Write find_index_by_value function which will check
    # if the tuple countries contains a country of your choice. If your_choice_country is in the tuple, return its
    # index, otherwise return a -1 value

    if your_choice_country == None or find_index_by_value(your_choice_country, countries) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = -1
    if your_choice_country in countries:
        result = countries.index(your_choice_country)
    assert find_index_by_value(your_choice_country, countries) == result


def test_find_value_by_index():
    # Change the previous exercise. Enter a random number and save it to variable your_choice_number. Write
    # find_value_by_index function which will check if the tuple countries contains a country with this index.
    # If there is a value with this index your_choice_number in the tuple, return this value,
    # otherwise return a 'No such index' text

    if your_choice_number == None or find_value_by_index(your_choice_number, countries) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = 'No such index'
    if 0 <= your_choice_number < len(countries):
        result = countries[your_choice_number]
    assert find_value_by_index(your_choice_number, countries) == result


def test_add_your_own_team():
    # Enter a pair of values in variables new_team_name, new_team_city. Then write add_your_own_team function
    # to add them to nhl_hockey_teams dictionary, where the name will be the key.

    if new_team_name == None or new_team_city == None or add_your_own_team(new_team_name, new_team_city) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    nhl_hockey_teams[new_team_name] = new_team_city
    assert add_your_own_team(your_choice_number, countries) == nhl_hockey_teams


def test_join_dicts():
    # Create two dictionaries in dict_1, dict_2 variables. Write a join_dicts function to concatenate the following
    # dictionaries to create a new one.

    if dict_1 == None or dict_2 == None or join_dicts(dict_1, dict_2) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert join_dicts(dict_1, dict_2) == dict_1.join(dict_2) or join_dicts(dict_1, dict_2) == dict_2.join(dict_1)


def test_create_numbers_dict():
    # # Enter a random number and save it to number_1 variable. Then write create_numbers_dict function to generate
    # a dictionary that contains items with keys from 1 to number_1 and values in format "x": "x**2".

    if number_1 == None or create_numbers_dict(number_1) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = {}
    for item in range(1, number_1 + 1):
        result[item] = item ** 2
    assert create_numbers_dict(number_1) == result


def test_sum_up_hockey_cups():
    # Write sum_up_hockey_cups functions to sum all values in a dictionary dict_3.

    if sum_up_hockey_cups(dict_3) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = 0
    for key in dict_3:
        result += dict_3[key]
    assert sum_up_hockey_cups(dict_3) == result


def test_remove_item_by_key():
    # Write remove_item_by_key function to remove a key True from dict_4 dictionary.

    if remove_item_by_key(dict_4) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    del dict_4[True]
    assert remove_item_by_key(dict_4) == dict_4


def test_find_min_max():
    # Write find_min_max function to get the maximum and minimum value in dict_5 dictionary. Return the answer in format
    # {
    #     "min": 111,
    #     "max": 222
    # }

    if find_min_max(dict_5) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = {}
    min_value = None
    max_value = None
    for item in dict_5:
        if dict_5[item] > max_value:
            max_value = dict_5[item]
        if dict_5[item] < min_value:
            min_value = dict_5[item]
    result['min'] = min_value
    result['max'] = max_value
    assert find_min_max(dict_5) == result


def test_remove_duplicates():
    # Write remove_duplicates functions to remove duplicates from dictionary dict_6.

    if remove_duplicates(dict_6) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    result = {}
    for key, value in dict_6.items():
        if value not in dict_6.values():
            result[key] = value
    assert remove_duplicates(dict_6) == result
