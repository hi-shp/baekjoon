import sys
input = sys.stdin.readline
N = int(input())
a = set(input().split())
M = int(input())
for x in input().split():
    if x in a:
        print('1')
    else:
        print('0')