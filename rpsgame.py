import random, sys

print('ROCK, PAPER, SCISSORS')

#Keep track of wins, draws, losses
wins = 0
draws = 0
losses = 0

while True: #main game loop
    print('%s wins, %s draws, %s losses' % (wins, draws, losses))
    while True: #player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #quit
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #break out of player move loop
        print('Type one of r, p, s or q')

    #Display player's input
    if playerMove == 'r':
        print('ROCK versus ')
    elif playerMove == 'p':
        print('PAPER versus ')
    elif playerMove == 's':
        print('SCISSORS versus ')

    #Dislapy what the comp chose
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        compMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        compMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        compMove = 's'
        print('SCISSORS')

    #Display and record w,d,l
    if playerMove == compMove:
        print('It is a DRAW.')
        draws = draws + 1
    elif playerMove == 'r' and compMove == 's':
        print('You WIN!')
        wins = wins + 1
    elif playerMove == 'p' and compMove == 'r':
        print('You WIN!')
        wins = wins + 1
    elif playerMove == 's' and compMove == 'p':
        print('You WIN!')
        wins = wins + 1
    elif playerMove == 'r' and compMove == 'p':
        print('You LOSE!')
        losses = losses + 1
    elif playerMove == 'p' and compMove == 's':
        print('You LOSE!')
        losses = losses + 1
    elif playerMove == 's' and compMove == 'r':
        print('You LOSE!')
        losses = losses + 1