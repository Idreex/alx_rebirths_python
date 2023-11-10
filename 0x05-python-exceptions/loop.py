import random
upper_bound = 20
lower_bound = 1
adaptive_upper_bound = upper_bound
adaptive_lower_bound = lower_bound
#to_be_guessed = int(n * random.random()) + 1
to_be_guessed = random.randint(lower_bound, upper_bound)
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess == 0: # giving up
        print("Sorry that you're givi ng up!")
        break # break out of a loop, don't execute "else"
    if guess < lower_bound or guess > upper_bound:
        print("guess not within boundaries!")
    elif guess < adaptive_lower_bound or guess > adaptive_upper_bound:
        print("Your guess is contradictory to your previous guesses!")
    elif guess > to_be_guessed:
        adaptive_upper_bound = guess - 1
        print("Number too large")
    elif guess < to_be_guessed:
        adaptive_lower_bound = guess + 1
        print("Number too small")
else:
    print("Congratulations. You made it!")
