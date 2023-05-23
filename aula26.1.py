num = int(input('Type a number between 1 and 5: '))
print('This will be the quantity of "i" at the end of the word "oi"')
oi= 'oi'
if num == 1:
    print(f'{oi: >10}')
elif num == 2:
    print(f'{oi:i<3}')
elif num == 3:
    print(f'{oi:i<4}')
elif num == 4:
    print(f'{oi:i<5}')
elif num == 5:
    print(f'{oi:i<6}')
else:
    print('You did not type a number between 1 and 5')
