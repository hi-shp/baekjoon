N = int(input())
k = []
for i in range((N//5)+1):
    h = 0
    x = N
    h += i
    x -= 5*i
    h += x // 3
    x = x % 3
    if x == 0:
        k.append(h)
if k == []:
    print(-1)
else:
    print(min(k))