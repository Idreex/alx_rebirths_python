#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary.update({key : value})
    print(a_dictionary)
 
    
    
    
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
key = 'language'
value = 'python'

update_dictionary(a_dictionary, 'city', "San Francisco")
update_dictionary(a_dictionary, 'language', "python")
