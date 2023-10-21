
def weight_average(my_list=[]):
    upp = 0
    low = 0
    for l in range(len(my_list)):
        for m in range(len(my_list[l])):
            upp += my_list[l][0] * my_list[l][1]
            low += my_list[l][1]
    print(upp)
    print(low)
    average = upp / low
    return average


my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]

print(weight_average(my_list))






