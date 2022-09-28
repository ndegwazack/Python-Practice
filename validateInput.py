while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a valid number.')

while True:
    print('Enter a password (Numbers and letters only)')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')