T = int(input())
j = list()
for _ in range(T):
    k = list(map(int, input().split()))
    k.sort(reverse=True)
    x = 0
    if k[0] == k[-1]:
        x = 1000*k[0]+10000
    else:
        for i in range(2):
            if k[i] == k[i+1]:
                x = 100 * k[i] + 1000
                break
            x = 100 * k[0]
    j.append(x)
j.sort(reverse=True)
print(j[0])