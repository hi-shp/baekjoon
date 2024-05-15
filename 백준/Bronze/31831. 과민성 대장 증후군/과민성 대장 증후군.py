N, M = map(int, input().split())
a = list(map(int, input().split()))
b = []
k = 0
for x in a:
    k += x
    if k <= 0:
        k = 0
    b.append(k)
k = 0
for x in b:
    if x >= M:
        k += 1
print(k)