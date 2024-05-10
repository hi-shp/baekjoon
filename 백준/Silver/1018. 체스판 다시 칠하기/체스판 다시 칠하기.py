N, M = map(int, input().split())
board = []
result = []
for _ in range(N):
    board.append(input())
for i in range(N-7):
    for j in range(M-7):
        w_need = 0
        b_need = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if board[x][y] == 'W':
                        b_need += 1
                    if board[x][y] == 'B':
                        w_need += 1
                else:
                    if board[x][y] == 'W':
                        w_need += 1
                    if board[x][y] == 'B':
                        b_need += 1
        result.append(w_need)
        result.append(b_need)
print(min(result))