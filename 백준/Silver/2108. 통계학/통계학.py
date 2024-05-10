import sys
input = sys.stdin.readline
T = int(input())
a = [int(input()) for _ in range(T)]
print(round(sum(a)/T))
a = sorted(a)
print(round(a[int((T-1)/2)]))
k = max(a) - min(a)
b = set(a)
b = list(b)
cnt = [a.count(x) for x in b]
if cnt.count(max(cnt)) > 1:
    c = []
    for i in range(len(cnt)):
        if cnt[i] == max(cnt):
            c.append(b[i])
    c = sorted(set(c))
    print(c[1])
else:
    print(b[cnt.index(max(cnt))])
print(k)