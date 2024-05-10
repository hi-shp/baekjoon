S = int(input())
a = 0
x = S - a
while a < x:
    x = x - a
    a += 1
    if a == x:
        print(a)
        break
else:
    print(a-1)