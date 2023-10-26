#!/usr/bin/python3

import turtle
# turtle.shape("turtle")
# for i in range(0,5):
#     turtle.forward(100)
#     turtle.right(72)
# turtle.exitonclick()

# total = 0
# while total < 30:
#     num = int(input('Enter a number: '))
#     total = total + num
# print('The total is', total)


a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}

def sort_dict(a_dictionary):
    sorted = list(a_dictionary.items())
    sorted.sort()
    sorted_dict = dict(sorted)
    return sorted_dict
print(sort_dict(a_dictionary))


def multi2(a_dictionary):
    newdict = sort_dict(a_dictionary)
    dict_2 = newdict.copy()
    for k, v in dict_2.items():
        dict_2[k] = v*2
    print(dict_2)
        

        
multi2(a_dictionary)