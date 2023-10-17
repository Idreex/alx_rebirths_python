#!/usr/bin/python3

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    
def multiply_by_2(a_dictionary):
    lst = []
    for k in a_dictionary.items():
        lst.append(k)
        lst.sort()
    for k,v in dict(lst).items():
        print(k,v)
    print("--")
    print("--")
    for k,v in dict(lst).items():
        print(k, v*2)
    
multiply_by_2 (a_dictionary)
    
