#"in" and "not in"

name = input('Type your name: ')
search = input('Type what you want to search in your name: ')

if search in name:
    print(f"{search} is in {name}")
else:
    print(f'{search} is not in {name}')
