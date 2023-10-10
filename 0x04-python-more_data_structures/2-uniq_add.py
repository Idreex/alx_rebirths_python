#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = set(my_list.copy())
    result = 0
    for i in new_list:
        result += i
    return result


my_list = [1, 2, 3, 1, 4, 2, 5]

print(uniq_add(my_list))

