n = int(input())
a = [str(input()) for _ in range(n)]
a = list(set(a))
a.sort()
a.sort(key=len)
for i in a:
    print(i)