a = []
for _ in range(5):
    a.append(list(input()))
for i in range(max([len(a[i]) for i in range(5)])):
    for j in range(5):
        try:
            print(a[j][i], end="")
        except:
            pass