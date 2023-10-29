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
        