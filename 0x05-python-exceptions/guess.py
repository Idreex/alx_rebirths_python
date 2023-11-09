import random

choice = random.choice([10,11,12,13,14])
# choice = random.choice(range(10,14))
gambler = int(input('Enter your guess num with 10 - 14\n'))
if gambler not in [10,11,12,13,14]:
    print('please follow instruction')

elif choice != gambler:
    print('sorry, you missed it the num is : ', choice)
    print('Try more')
else:
    gambler == choice
    print('Congratulations, I was thinking number: ', choice)

