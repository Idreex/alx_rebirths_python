d1 = {"foo":34, "bar": 23}
d2 = {"dev": 21, "bar":54}

def dict_merge_sum(d1, d2):
    m = d1.copy()
    for v in d2.values():
        if d2.values() == m.values():
            sum(d2.keys(), m.keys())
    m.update(d2)

    return m
print(dict_merge_sum(d1,d2))


supermarket = { "milk": {"quantity": 20, "price": 1.19},
               "biscuits":  {"quantity": 32, "price": 1.45},
               "butter":  {"quantity": 20, "price": 2.29},
               "cheese":  {"quantity": 15, "price": 1.90},
               "bread":  {"quantity": 15, "price": 2.59},
               "cookies":  {"quantity": 20, "price": 4.99},
               "yogurt": {"quantity": 18, "price": 3.65},
               "apples":  {"quantity": 35, "price": 3.15},
               "oranges":  {"quantity": 40, "price": 0.99},
               "bananas": {"quantity": 23, "price": 1.29}}

print(supermarket["milk"]["quantity"]*supermarket["milk"]["price"])


d = {"a":123, "b":34, "c":304, "d":99}
for key in d:
    print(d[key])


