#!/usr/bin/python3

my_list = [8,2,6]
idx = 2
element = [4,9]


def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list) -1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
    
def extend_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    else:
        my_list + element
        return my_list
    
def add_frm_left(my_list, idx, element):
    if idx < 0: 
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    else: 
        my_list[:0] = element
        return my_list


print(new_in_list(my_list, idx, element))
print(extend_in_list(my_list, idx, element))
print(add_frm_left(my_list, idx, element))