#!/usr/bin/python3


# def print_reversed_list_integer(my_list=[]):
#     for i in my_list[::-1]:
#         print(i)
    

# my_list = [1,2,3,4,5]
# print_reversed_list_integer(my_list)

if __name__ == "__main__":
    import sys

    for i in range(len(sys.argv) - 1):
        if len(sys.argv) == 0:
            print("{} : argument".format(i))
        if len(sys.argv) == 1:
            print("{} : argument".format(i))
        else:
            if len(sys.argv) != 0:
                i = 0
                print("{} : {}".format(i, sys.argv))
            i += 1
        
