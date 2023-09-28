#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list

my_list = [2,4,6,8]
idx = -1
element = 9

print("{}".format(replace_in_list(my_list, idx, element)))

# my_list = [2,4,6,8]
# pos = -4
# item = 9

# def insert_in_list(my_list, pos, item):
#     if pos < 0:
#         return my_list[pos]
    
#     elif pos >= len(my_list) - 1:
#         my_list = my_list + [item]
#         return my_list
    
    

    
# t = insert_in_list(my_list, pos, item)
# print(t)