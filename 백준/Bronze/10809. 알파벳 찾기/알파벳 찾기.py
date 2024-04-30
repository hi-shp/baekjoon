a = list(str(input()))
word = []
k = []
for i in range(97, 123):
    word.append(chr(i))
    k.append(-1)
for x in a:
    if x in word:
        if k[word.index(x)] == -1:
            k[word.index(x)] = a.index(x)
print(*k)