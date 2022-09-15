print('Enter your password.')
typedPassword = input()
if typedPassword == 'swordfish':
    print('Access Granted')
elif typedPassword == 'mary':
    print('Hint: the password is a fish.')
elif typedPassword == '12345':
    print('Nice try.')
else:
    print('Access Denied')
print('Done')