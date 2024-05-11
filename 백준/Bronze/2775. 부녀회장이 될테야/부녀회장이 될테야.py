import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    a = int(input())
    b = int(input())
    k = [i for i in range(1, b + 1)]
    for x in range(a):
        h = 0
        for y in range(b):
            h += k[y]
            k[y] = h
    print(k[-1])