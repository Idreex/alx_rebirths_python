def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in my_l_1:
            for j in my_l_2:
                res = i / j
                new_list.append(res)
            else:

                j <= 0 or type(j) == str
                res = 0
                new_list.append(res)

    except Exception as e:
        err = j
        print('Can not divide by {}'.format(err))
    
    finally:
        print('result is: {}'.format(new_list))
    
    
    
# my_l_1 = [10, 8, 4]
# my_l_2 = [2, 4, 4]


my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]

list_division(my_l_1,my_l_2, 3)


