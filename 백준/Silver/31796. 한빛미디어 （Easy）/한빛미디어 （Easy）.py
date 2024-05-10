import sys
input = sys.stdin.readline
N = int(input())
if N != 1:
    a = list(map(int, input().split()))
    a.sort()
    t = []
    x = a[0]
    k = 0
    for i in range(N):
        if a[i] >= 2*x:
            k += 1
            x = a[i]
    t.append(k)
    print(max(t)+1)
else:
    print(1)