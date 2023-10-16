#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary.update('language':'Python')
 
    a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }




def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

items = [1,3,5,9]
print(sum(items))



def sum(*args):
    total = 0
    for arg in args:
        total += arg
    
    return total

#args = [1,2,3,4]

print(sum(9,2,3,4))