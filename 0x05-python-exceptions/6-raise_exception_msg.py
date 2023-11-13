def raise_exception_msg(message=""):
    try:
        if type(message) != str:
            print(message)
            raise NameError
        else:    
            print(message)
            return True
    except NameError:
        print('NameError: Type mismatch ')
    finally:
        print('The argument is', message)
    
    
raise_exception_msg(23)