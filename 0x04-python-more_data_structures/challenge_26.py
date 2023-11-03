#!/usr/bin/python3
'''026
Pig Latin takes the first consonant of a word, 
moves it to the end of the word and adds on an 
“ay”. If a word begins with a vowel you just add 
“way” to the end. For example, pig becomes igpay, 
banana becomes ananabay, and aadvark becomes 
aadvarkway. Create a program that will ask the 
user to enter a word and change it into Pig Latin. 
Make sure the new word is displayed in lower case.'''

def latin(word):
    if word[0] in ['a','e','i','o','u']:
        res = word + 'way'
    else:
        res = word[1:] + word[0] + 'ay'

    return res
print(latin('aadvark'))
print() 

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    new = []
    for i in row:
        new.append(i)
    print(new)
print()
for row in matrix:
    new = []
    for i in row:
        new.append(i*i)
    print(new)


def weight_average(my_list=[]):
    up = 0
    dw = 0
    for i in range(len(my_list)):
        res = my_list[i][0] * my_list[i][1]
        up += res
        re = my_list[i][1]
        dw += re
    return up/dw

my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
print(weight_average(my_list))


