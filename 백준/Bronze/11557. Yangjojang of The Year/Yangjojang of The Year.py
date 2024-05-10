T = int(input())
for i in range(T):
    t = int(input())
    namelist = numlist = list()
    dic = {}
    for j in range(t):
        name, num = input().split()
        num = int(num)
        dic[num] = name
        numlist.append(num)
    numlist.sort(reverse=True)
    print(dic[numlist[0]])