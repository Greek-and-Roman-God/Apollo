# 12360 DFS와 BFS
# https://www.acmicpc.net/problem/1260
n, m, v = map(int, input().split())
checked = [0]*n
board = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    board[x][y] = 1
    board[y][x] = 1


# def dfs(i):

#     if not any(checked):
#         print()
#         return

#     for j, b in enumerate(board[i]):
#         if checked[j] == 0 and b == 1:
#             checked[j] = 1
#             print(j+1, end=' ')
#             dfs(j)


# print(v, end=' ')
# checked[v-1] = 1
# dfs(v-1)

# checked = [0]*(n+1)


# def bfs(v):
#     queue = [v]
#     checked[v] = 1

#     while queue:
#         num = queue.pop(0)
#         print(num, end=' ')
#         for i in range(1, n+1):
#             if checked[i] == 0 and board[num-1][i-1] == 1:
#                 queue.append(i)
#                 checked[i] = 1


# bfs(v)


#
checked = [0]*(n+1)


def dfs(i):
    checked[i] = 1
    print(i, end=' ')
    for j in range(1, n+1):
        if checked[j] == 0 and board[i][j] == 1:
            dfs(j)


def bfs(v):
    queue = [v]
    checked[v] = 0

    while queue:
        num = queue.pop(0)
        print(num, end=' ')
        for i in range(1, n+1):
            if checked[i] == 1 and board[num][i] == 1:
                queue.append(i)
                checked[i] = 0


dfs(v)
print()
bfs(v)
