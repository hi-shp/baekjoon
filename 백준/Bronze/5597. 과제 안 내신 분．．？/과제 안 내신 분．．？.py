a = [i for i in range(1,31)]
for _ in range(28):
    k = int(input())
    a.remove(k)
print(a[0])
print(a[1])