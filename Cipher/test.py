i = 0
spam = 'Hello'
while i < 5:
    spam = spam + spam[i]
    i = i + 1
print(spam)

j = 0
while j < 4:
    while j < 6:
        j += 2
        print(j)

spam = 'foo'
for i in spam:
    spam = spam + i
print(spam)

if 10 < 5:
    print('Hello')
elif False:
    print('Alice')
elif 5 != 5:
    print('Bob')
else:
    print('Goodbye')

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