#!/usr/bin/python3

def no_c(my_string):
    max_len = len(my_string)
    result = ''
    for i in range(max_len):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        result += my_string[i]
    return result
my_string = 'chocolate'

print(no_c(my_string))
print(no_c('Best School'))
print(no_c('Chicago'))
print(no_c('Coconut'))


