birthdays = {'Alice' : 'Apr 1', 'Bob' : 'Dec 25', 'Carol' : 'Jan 1'}

while True:
    print('Enter a name: (Blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('No birthday info for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthdays database updated.')
print(birthdays)