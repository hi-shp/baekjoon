n = int(input())
k = 1
result = []
while True:
    a = list(str(k))
    b = [int(x) for x in a]
    if k == n:
        if len(result) == 0:
            result.append(0)
        break
    if sum(b) + k == n:
        result.append(k)
        k += 1
    else:
        k += 1
print(min(result))