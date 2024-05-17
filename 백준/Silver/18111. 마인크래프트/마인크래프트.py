import sys
N, M, B = map(int, sys.stdin.readline().split())
a = []
for _ in range(N):
    a.extend(map(int, sys.stdin.readline().split()))
time = [0 for i in range(257)]
h = 0
for x in range(257):
    block = B
    for i in a:
        if i <= x:
            time[x] += x - i
            block -= x - i
        else:
            time[x] += 2 * (i - x)
            block += i - x
    if block >= 0 and time[x] <= time[h]:
        h = x
print(time[h], h)