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