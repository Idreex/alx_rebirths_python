#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    lst_dict = []
    for key in a_dictionary.items():
        lst_dict.append(key)
        lst_dict.sort()
    print(dict(lst_dict))


a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }

sorted = sorted(a_dictionary.items())

print(sorted)
print_sorted_dictionary(a_dictionary)

