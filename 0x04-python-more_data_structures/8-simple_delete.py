#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    del a_dictionary[key]
    return a_dictionary


a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
print(simple_delete(a_dictionary, key="Number"))