#!/usr/bin/python3

def add_tuple(tuple_a=(0,0), tuple_b=(0,0)):
    new_tuple = []

    

    new_tuple.append(tuple_a[0] + tuple_b[0])
    new_tuple.append(tuple_a[1] + tuple_b[1])
    result = tuple(new_tuple)
    return result


tuple_a = (1, )
tuple_b = (88, 11)

print(add_tuple(tuple_a, tuple_b))

