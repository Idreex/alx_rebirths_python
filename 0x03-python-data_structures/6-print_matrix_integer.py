#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for item in row:
            if item == row[-1]:
                print("{:d}".format(item), end="")
            else:
                print("{:d}".format(item), end=" ")
            print()
            

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

''' if we want it to print inside list that could be like this'''
def matrix_int_lists(matrix=[[]]):
    for row in matrix:
        new_matrix = []
        for element in row:
            new_matrix.append(element)
        print(new_matrix)

print('\n')
print('\n')

''' if we want it to print inside list that could be like this'''
def matrix_int_listd(matrix=[[]]):
    for row in matrix:
        new_matrix = []
        for element in row:
            new_matrix.append(element*element)
        print(new_matrix)

print_matrix_integer(matrix)
matrix_int_lists(matrix)
matrix_int_listd(matrix)