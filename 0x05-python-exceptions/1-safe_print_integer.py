def safe_print_integer(value):
    try:
        if type(value) == int :
            print(f'{value} is an integer:')
            return True
        else:
            print(f'{value} is not an integer:')
            return False   
    except TypeError:
        print(f'wrong value type: {value}')


safe_print_integer(-89)
