a = []
for _ in range(10):
    a.append(int(input())%42)
a.sort()
k = 10
for i in range(9):
    if a[i] == a[i+1]:
        k -= 1
print(k)