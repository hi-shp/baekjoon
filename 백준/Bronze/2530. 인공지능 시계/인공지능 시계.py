a, b, c = map(int, input().split())
d = int(input())
hr = a
min = b
sec = c+d
if sec >= 60:
    min = b + sec // 60
    sec = sec % 60
    if min >= 60:
        hr = a + min // 60
        min = min % 60
        if hr >= 24:
            hr = hr%24
print(hr, min, sec)