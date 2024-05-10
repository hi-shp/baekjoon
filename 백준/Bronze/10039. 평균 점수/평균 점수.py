b = 0
for _ in range(5):
    a = int(input())
    if a >= 40:
        b += a
    else:
        b += 40
print(format(b/5, ".0f"))