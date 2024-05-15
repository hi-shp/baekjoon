a = []
M = 0
garo = 0
for i in range(9):
    x = list(map(int, input().split()))
    a.append(x)
    for k in x:
        if k > M:
            M = k
            garo = i+1
print(M)
if M == 0:
    print(1,1)
else:
    print(garo, a[garo-1].index(M)+1)