N = int(input())
total = 0
for _ in range(N):
    a = list(input())
    b = set(a)
    a0 = a[0]
    k = 0
    for x in a:
        if x != a0:
            k += 1
        a0 = x
    if k+1 == len(b):
        total += 1
print(total)