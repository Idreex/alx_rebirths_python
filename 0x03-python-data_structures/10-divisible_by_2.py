#!/usr/bin/python3  

def divisible_by_2(my_list=[]):
    
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            print(f'{my_list[i]} is divisible by 2')
        else:
            print(f'{my_list[i]} is not divisible by 2')

if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5, 6]
    divisible_by_2(my_list)