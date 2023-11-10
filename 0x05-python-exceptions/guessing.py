import random
upper_bound = 20
lower_bound = 1
#to_be_guessed = int(n * random.random()) + 1
to_be_guessed = random.randint(lower_bound, upper_bound)
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
        else:
        # 0 means giving up
            print("Sorry that you're giving up!")
        break # break out of a loop, don't execute "else"
else:
    print("Congratulations. You made it!")