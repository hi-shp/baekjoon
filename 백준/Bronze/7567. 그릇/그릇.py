a = list(input())
x = 10
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        x += 5
    else:
        x += 10
print(x)