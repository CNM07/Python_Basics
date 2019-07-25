#Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user

user_input = input('Please enter a number: ')
if int(user_input) % 2 == 0:
    print('This number is EVEN')
else:
    print('This number is ODD')


user_input = input('Please enter a number: ')
if int(user_input) % 2 == 0 and not int(user_input) % 4 == 0:
    print('This number is EVEN')
elif int(user_input) % 4 == 0:
    print('This is a multiple of four')
else:
    print('This number is ODD')
