# 2580 스도쿠
# https://www.acmicpc.net/problem/2580


# board = [list(map(int, input().split())) for _ in range(9)]
board = [
    [0, 3, 5, 4, 6, 9, 2, 7, 8],
    [7, 8, 2, 1, 0, 5, 6, 0, 9],
    [0, 6, 0, 2, 7, 8, 1, 3, 5],
    [3, 2, 1, 0, 4, 6, 8, 9, 7],
    [8, 0, 4, 9, 1, 3, 5, 0, 6],
    [5, 9, 6, 8, 2, 0, 4, 1, 3],
    [9, 1, 7, 6, 5, 2, 0, 8, 0],
    [6, 0, 3, 7, 0, 1, 9, 5, 2],
    [2, 5, 8, 3, 9, 4, 7, 6, 0],
]
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]


def is_promising(i, j):
    promising = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 행렬 검사
    for k in range(9):
        if board[i][k] in promising:
            promising.remove(board[i][k])
        if board[k][j] in promising:
            promising.remove(board[k][j])

    # 박스 검사
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if board[p][q] in promising:
                promising.remove(board[p][q])
    return promising


flag = False


def dfs(x):
    global flag

    if flag:
        return

    if x == len(zeros):
        for row in board:
            print(*row)
        flag = True
        return
    else:
        (i, j) = zeros[x]
        promising = is_promising(i, j)

        for num in promising:
            board[i][j] = num
            dfs(x+1)
            board[i][j] = 0


dfs(0)
