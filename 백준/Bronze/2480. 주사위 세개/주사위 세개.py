k = list(map(int,input().split()))
def func (a):
    a.sort(reverse=True)
    if a[0]==a[1]==a[2]:
        x = 1000*a[0]+10000
    else:
        x = 100 * a[0]
        for i in range(2):
            if a[i] == a[i+1]:
                x = 100*a[i]+1000
    return x
print(func(k))