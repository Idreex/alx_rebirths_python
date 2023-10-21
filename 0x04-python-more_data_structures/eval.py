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

total_value = 0
for article in supermarket:
    quantity = supermarket[article]["quantity"]
    price = supermarket[article]["price"]
    total_value += quantity * price

print(f"The total price for buying everything: {total_value:7.2f}")


# def dict_merge_sum(d1, d2):
#     """ Merging and calculating the sum of two dictionaries: 
#     Two dicionaries d1 and d2 with numerical values and
#     possibly disjoint keys are merged and the values are added if
#     the exist in both values, otherwise the missing value is taken to
#     be 0"""
    
#     merged_sum = d1.copy()
#     for key, value in d2.items():
#         if key in d1:
#             d1[key] += value
#         else:
#             d1[key] = value
    
#     return merged_sum

# d1 = dict(a=4, b=5, d=8)
# d2 = dict(a=1, d=10, e=9)

# print(dict_merge_sum(d1, d2))


def dict_sum(d1, d2):
    """  Merging and calculating the sum of two dictionaries: 
    Two dicionaries d1 and d2 with numerical values and
    possibly disjoint keys are merged and the values are added if
    the exist in both values, otherwise the missing value is taken to
    be 0"""
    
    return { k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1) | set(d2) }

d1 = dict(a=4, b=5, d=8)
d2 = dict(a=1, d=10, e=9)

print(dict_merge_sum(d1, d2))
