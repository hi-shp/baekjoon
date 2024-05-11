import sys
input = sys.stdin.readline
N, M = map(int, input().split())
a = list(map(int, input().split()))
k = 0
for x in range(len(a)-2):
    x = a[x]
    for y in range(a.index(x)+1, len(a)-1):
        y = a[y]
        for z in range(a.index(y)+1, len(a)):
            z = a[z]
            if M-(x+y+z) >= 0 and x+y+z >= k:
                k = x + y + z
print(k)