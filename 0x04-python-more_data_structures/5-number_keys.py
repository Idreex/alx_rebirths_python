#!/usr/bin/python3

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
def number_keys(a_dictionary):
    
    lst_dict = list(a_dictionary)
    print(len(lst_dict))

# OR

    nb_keys = len(a_dictionary)
    print(nb_keys)
    
# OR 
nb_keys = 0
for key in a_dictionary.keys():
    print(key)
    nb_keys += 1
print(nb_keys)

# for Values:
nb_values = 0
for value in a_dictionary.values():
    nb_values += 1
print(nb_values)
number_keys(a_dictionary)
    
