#execício

name = input('What is you name? ')
age = input('What is your age? ')

if name and age:
    print(f"Your name's: {name}")
    print('Your name inverted is:', name[ : :-1])


    if " " in name:
        print("Your name contains spaces")
    else:
        print('Your name does not contain spaces')

        
    print("Your name has", len(name), "letters")
    print("The first letter of your name is:", name[0])
    print("The last letter of your name is:", name[-1])
else:
    print("I'm sorry, you left empty fields")