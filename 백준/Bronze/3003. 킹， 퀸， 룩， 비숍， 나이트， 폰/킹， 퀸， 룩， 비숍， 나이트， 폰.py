a = [1, 1, 2, 2, 2, 8]
b = list(map(int, input().split()))
k = []
i = 0
for x in b:
        k.append(a[i]-x)
        i += 1
print(*k)