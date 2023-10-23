#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda y: y * y, x)), matrix))

# or


def square_matrix(matrix):
    # Define a function to square an integer
    def square(x):
        return x ** 2
    # Use the map function to apply the square function to each element in the matrix
    squared_matrix = list(map(lambda row: list(map(square, row)), matrix))
    
    return squared_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(square_matrix(matrix))