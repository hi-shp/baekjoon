a = list(map(int, input().split()))
k = 0
for x in a:
    x = x ** 2
    k += x
print(k%10)