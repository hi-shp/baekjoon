a = input().lower()
word = []
count = [1 for i in range(len(set(a)))]
for x in a:
    i = 1
    if x not in word:
        word.append(x)
    else:
        count[word.index(x)] += i
if count.count(max(count)) == 1:
    print(word[count.index(max(count))].upper())
else:
    print('?')