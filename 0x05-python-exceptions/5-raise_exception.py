def raise_exception():
    try:
        if type() != int:
            print('It\'s not int')
            raise Exception
        else:
            print('You good to go')
            return True
    except Exception as e:
        print("TypeError: Data type mismatch")

def check(a):
    raise_exception() 
a  = 3
# a = 'str'
check(a)



