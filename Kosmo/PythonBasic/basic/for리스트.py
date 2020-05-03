# for i in range(A,B,C=1)
# for( int i = A ; i < B ; i = i + C )

# print( end ='' )

for x in range(1, 11):
    print(x, end=' ')
print()

for x in range(1, 11, 2):
    print(x, end=' ')
print()

for x in range(1, 101, 5):
    print(x, end=' ')
print()

for x in range(10, 0, -1):
    print(x, end=' ')
print()

lang = ['자바', '파이썬', 'GO']
for i in range(0, len(lang)):
    print(str(i) + '번 - ' + lang[i])
print()

for x in lang:
    print(x, end=' ')
