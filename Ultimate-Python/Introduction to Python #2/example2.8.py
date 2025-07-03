#Python Script 32
#Deciding whether a name starts by a vowel

myWord = input('Please input your name: ')

if myWord.startswith('A') or \
     myWord.startswith('E') or \
     myWord.startswith('I') or \
     myWord.startswith('O') or \
     myWord.startswith('U'):
     print('Hello,', myWord,'!')
else:
     print('Hello')