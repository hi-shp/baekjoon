a = list(input())
b = []
for x in a:
    if x.isupper() == True:
        b.append(x.lower())
    else:
        b.append(x.upper())
print(''.join(b))