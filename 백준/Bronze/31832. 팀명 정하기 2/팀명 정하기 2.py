N = int(input())
a = [input() for _ in range(N)]
for x in a:
    low, up, num, hype = 0, 0, 0, 0
    for y in x:
        if 97 <= ord(y) and ord(y) <= 122:
            low += 1
        elif 65 <= ord(y) and ord(y) <= 90:
            up += 1
        elif 48 <= ord(y) and ord(y) <= 57:
            num += 1
        elif ord(y) == 45:
            hype += 1
    if up <= low and low+up+num+hype <= 10 and up+low+hype != 0:
        result = x
        break
print(result)