from random import choice
from string import digits

code = list()
for i in range(6):
    code.append(choice(digits))

print ''.join(code)

#to run code press down on cmd + i#
