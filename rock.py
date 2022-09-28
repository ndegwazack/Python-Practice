import random, sys

wins = 0
ties = 0
losses = 0

while True:
    print(f'{wins} wins, {ties} ties, {losses} losses')
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        move = input()
        if move == 'q':
            sys.exit()
        if move == 'r' or move == 'p' or move == 's':
            break
        print('Enter one of p, q, r or s')

    if move == 'r':
        print('ROCK versus ...')
    elif move == 'p':
        print('PAPER versus ...')
    elif move == 's':
        print('SCISSORS versus ...')

    randomNum = random.randint(1, 3)
    if randomNum == 1:
        compMove = 'r'
        print('ROCK')
    elif randomNum == 2:
        compMove = 'p'
        print('PAPER')
    elif randomNum == 3:
        compMove = 's'
        print('SCISSORS')
    
    if move == compMove:
        print('It is a tie!')
        ties += 1
    elif move == 'r' and compMove == 's':
        print('You win!')
        wins += 1
    elif move == 'p' and compMove == 'r':
        print('You win!')
        wins += 1
    elif move == 's' and compMove == 'p':
        print('You win!')
        wins += 1
    elif move == 'r' and compMove == 'p':
        print('You lose!')
        losses += 1
    elif move == 'p' and compMove == 's':
        print('You lose!')
        losses += 1
    elif move == 's' and compMove == 'r':
        print('You lose!')
        losses += 1
