def safe_print_division(a, b):
    try:
        if b <= 0:
            a / b
            result = None
        else:
            result = a / b
        print(f'{a} / {b} = {result}')
    except ZeroDivisionError :
        result = None
        print(f'You can\'t divide by zero: {a} / {b} = {result} ')
    finally:
        print(f'Inside result: {result}')
        

 
a = 12
b = 2
safe_print_division(a, b)
# print("{:d} / {:d} = {}".format(a, b, result))
