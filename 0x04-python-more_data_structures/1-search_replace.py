#!/usr/bin/python3





def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(0, len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    print(my_list)
    return new_list
    
my_list = [1,2,3,4,5]
search = 5
replace = 9
        
print(search_replace(my_list, search, replace))