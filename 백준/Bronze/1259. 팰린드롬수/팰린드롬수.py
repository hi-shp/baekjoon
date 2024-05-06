while True:
    k = str(input())
    if k == '0':
        break
    a = list(k)
    b = list(k)
    for i in range(int(len(b)/2)):
        b[i], b[len(b)-i-1] = b[len(b)-i-1], b[i]
    if a == b:
        print('yes')
    else:
        print('no')