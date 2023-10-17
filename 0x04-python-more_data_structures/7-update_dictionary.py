#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary.update({key : value})
    print(a_dictionary)
 
    
    
    
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
key = 'track'
value = 'high level'

update_dictionary(a_dictionary, key, value)
