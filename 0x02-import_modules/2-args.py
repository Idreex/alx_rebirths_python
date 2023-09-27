#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    i = len(sys.argv) - 1   

    if i == 0: 
         print("{} : argument".format(i))
    else:
        print(f"{i} : arguments")
        if i >= 1:
            count = 0
            for arg in sys.argv:
                if arg != sys.argv[0]:
                    print("{} : {}".format(count, arg))
                count += 1



    