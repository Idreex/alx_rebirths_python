#!/usr/bin/python3
from calculator_1 import add, sub, mult, div

if __name__ == "__main__":
    import sys
    
    t = input("<a> <operator> <b>\n") 
    while True:
        if t not in ["+", "-", "/", "*"]:
            print("\nUnknown operator. Available operators: +, -, * and / \n")
        break

a = int(input("\nEnter your values\n"))
b = int(input("\nEnter your values\n"))

if t == "+":
    print(add(a, b))
elif t == "-":
    print(sub(a,b))
elif t == "*":
    print(mult(a, b))
elif t == "/":  
    print(div(a, b))


    

