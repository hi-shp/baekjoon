N = int(input())
a = list(map(int, input().split()))
k = 0
for x in a:
    k += x/max(a)*100
print(k/N)