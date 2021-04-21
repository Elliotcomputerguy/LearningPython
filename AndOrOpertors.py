
#And, or operators
# and, or, not are logical operators. When combined with simple conditions they become compound conditions 

username = ''
password = ''

while not username:
    username = input('Enter your username:')   

while not password:
    password = input('Enter your password:')

if username == 'string' and password == 'string' or username == 'string0' and password == 'string0':
    print('Access granted')
elif username == 'string1' or password == 'string1':
    print('Access granted')
else:
    print('Access denied')
