allGuests = {
    'Alice': {'apples': 5, 'pringles': 12},
    'Bob' : {'sandwiches': 6, 'cakes': 9},
    'Carol' : {'cups': 3, 'pies': 5}
}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Pringles ' + str(totalBrought(allGuests, 'pringles')))