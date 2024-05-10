N = int(input())
k = 1
for i in range(1, N+1):
    k *= i
k = reversed(list(str(k)))
cnt = 0
for x in k:
    if x == '0':
        cnt += 1
    else:
        break
print(cnt)