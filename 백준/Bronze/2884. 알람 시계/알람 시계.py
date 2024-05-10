a, b = map(int, input().split())
h, m = 0, 0
b -= 45
if b < 0:
    m = 60+b
    a -= 1
    if a < 0:
        h = 23
    else:
        h = a
else:
    m = b
    h = a
print(h, m)
