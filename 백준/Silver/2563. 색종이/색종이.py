total = 0
a = [[0]*100 for _ in range(100)]
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            a[i-1][j-1] += 1
for k in a:
    for i in range(1, N+1):
        total += k.count(i)
print(int(total))