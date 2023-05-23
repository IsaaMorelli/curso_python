#exercício com if e comparação

value1 = input('Please type the first number: ')
value2 = input('Please type the second number: ')

if value2 < value1:
    print(f"The first number='{value1}'' is greater than the second number='{value2}'")
elif value2 > value1:
    print(f"The second number='{value2}' is greater than the first number='{value1}'")
