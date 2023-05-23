#operador lógico 'and'

value = input('Type "in" to log in or type "out" to log out: ')
password = input('Please type your password to continue: ')

password_confirmation = 'isa123'

if value == 'in' and password == password_confirmation:
    print("You entered the page. You're welcome!")
elif value == 'out' and password == password_confirmation:
    print('You left the page. See you again!')
else:
    print('Something went wrong. Please try again')