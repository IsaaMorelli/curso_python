"""
 012345678
 duck wolf
-987654321
"""


words = input('Type two words with 4 letters each: ')
print(" ")
print("which word would you like to display?")
num = input("Type '1' for the first word and '2' for the second word: ")

if num == '1':
    print(words[:4])
else:
    print(words[5:])