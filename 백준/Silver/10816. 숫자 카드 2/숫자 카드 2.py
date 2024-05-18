import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
dic = {}
for x in a:
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1
M = int(input())
b = list(map(int, input().split()))
for x in b:
    result = dic.get(x, 0)
    print(result, end=' ')