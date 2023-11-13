def safe_print_list_integers(my_list=[], x=0):
    try:    
        # for i in my_list:
        for i in range(x):
            if type(my_list[i]) == int:
                print(my_list[i], end="")
            else:
                continue
    except Exception as e:
        print()
        print('Index out of range')


my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
x = 8
safe_print_list_integers(my_list, x)
