a = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = list(str(input()))
k = 0
for i in word:
    for j in range(len(a)):
        if i in list(str(a[j])):
            k += a.index(a[j])+3
print(k)