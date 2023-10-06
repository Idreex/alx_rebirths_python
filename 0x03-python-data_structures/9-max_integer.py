#!/usr/bin/python3

def max_integer(my_list=[]):

    for i in range(len(my_list) -1):

        if my_list[i] > my_list[i+1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
            # tmp = my_list[i]
            # my_list[i] = my_list[i+1]
            # my_list[i+1] = tmp
        

if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_integer(my_list)
    print(my_list[-1]) 
    