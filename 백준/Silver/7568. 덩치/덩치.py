N = int(input())
result = [0]*N
x, y = [], []
for _ in range(N):
    X, Y = map(int, input().split())
    x.append(X), y.append(Y)
for i in range(len(x)):
    k = 0
    for j in range(len(x)):
        if x[i] < x[j] and y[i] < y[j]:
            k += 1
    result[i] = k+1
print(*result)