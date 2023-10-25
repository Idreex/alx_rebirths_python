#!/usr/bin/python3

import turtle
turtle.shape("turtle")
for i in range(0,5):
    turtle.forward(100)
    turtle.right(72)
turtle.exitonclick()

total = 0
while total < 30:
    num = int(input('Enter a number: '))
    total = total + num
print('The total is', total)