#if elif and else
#com = input("Type enter or exit: ")

#if com == 'enter':
    #print('you have entered the website')
#elif com == 'exit':
    #print('you have left the website')
#else:
    #print('you did not write the right word')
    #print('please type again')
    #com = input("Type enter or exit: ")

num = int(input('Type a number: '))
num_rest = num % 2

if num_rest == 0:
    print('This number is even')
elif num_rest == 1:
    print('This number is odd')