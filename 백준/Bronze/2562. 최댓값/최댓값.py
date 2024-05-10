a = list()
while True:
    try:
        q = int(input())
        a.append(q)
    except:
        break
print(max(a))
print(a.index(max(a))+1)