import random

secretnum = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretnum:
        print('Your guess is too low. \n Take another guess.')
    elif guess > secretnum:
        print('Your guess is too high. \n Take another guess.')
    else:
        break

if guess == secretnum:
    print('Good job, you got it right in ' + str(guessesTaken) + ' guesses!')
else:
    print('The number I had in mind was ', + str(secretnum))


