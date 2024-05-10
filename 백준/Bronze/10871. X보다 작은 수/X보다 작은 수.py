N, X = map(int, input().split())
a = list(map(int, input().split()))
for x in a:
    if x < X:
        print(x,'',end='')