#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    
   if idx < 0:
      return my_list
   if idx > len(my_list):
      return my_list
   else:
      del my_list[idx]
      return my_list

    
my_list = [1, 2, 3, 4, 5]
idx = 3
print(delete_at(my_list, idx))
