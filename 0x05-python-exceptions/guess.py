import random
import sys

choice = random.choice([10,11,12,13,14])
# choice = random.choice(range(10,14))
gambler = 0
chance = 0
expected = [10,11,12,13,14]

print('You have 3 chances in this game, carefully choose')
print('Press 0 to quit')

while True:
    gambler = int(input('Enter your guess num within range of 10 - 14\n'))
    

































#     if gambler == 0:
#         if gambler not in expected:
#             if chance == 0:
#                 print('You have not played')
#                 continue
#             elif gambler < choice or gambler > choice:
#                 print('sorry, you missed it the num is : ', choice)
#                 print('Try more')
#             elif gambler == choice:
#                 print('congratulations, you made it')
#             print('Follow the rules, you are expected to guess num within range of 10 - 14')
#             break
#         print('You gave up the game, see you next time')
#         sys.exit()
# else:
#     print('Keep striving everyday for daily progress')

