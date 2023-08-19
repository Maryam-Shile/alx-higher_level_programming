#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dict = dict(sorted(a_dictionary.items()))
    for x, y in sort_dict.items():
        print(x + ":", y)
