#!/usr/bin/python3

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
def number_keys(a_dictionary):
    
    lst_dict = list(a_dictionary)
    print(len(lst_dict))

# OR

    nb_keys = len(a_dictionary)
    print(nb_keys)
    

number_keys(a_dictionary)
    
