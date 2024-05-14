N = int(input())
for _ in range(N):
    stack = []
    for x in input():
        if x =='(':
            stack.append(x)
        else:
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(x)
                break
    if stack:
        print('NO')
    else:
        print('YES')