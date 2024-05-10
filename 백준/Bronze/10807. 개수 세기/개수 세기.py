N = int(input())
a = list(map(int, input().split()))
v = int(input())
k = 0
for i in range(N):
    if a[i] == v:
        k += 1
print(k)