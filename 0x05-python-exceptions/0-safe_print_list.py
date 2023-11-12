#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
    except IndexError as e:
        print('Index not exist')
        


my_list = [1, 2, 3, 4, 5]
safe_print_list()