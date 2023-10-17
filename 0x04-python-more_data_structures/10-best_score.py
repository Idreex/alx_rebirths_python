#!/usr/bin/python3

def best_score(a_dictionary):
    d = a_dictionary
    if d == None:
        return None
    lst = []
    lst2 = []
    for v in  list(d.items()):
        lst.append(v)
        lst.sort()

    for value in d.values():
        lst2.append(value)
        lst2.sort()
    print(f"Best_Score: {lst2[-1]}")
    print(dict(lst))

    
a_dictionary = {'John': 52, 'Bob': 94, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_score(a_dictionary)