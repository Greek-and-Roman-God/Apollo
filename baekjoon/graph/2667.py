# 2667 단지번호붙이기
# https://www.acmicpc.net/problem/2667

n = int(input())
mat = [list(input()) for _ in range(n)]
# mat = [
#     [0, 1, 1, 0, 1, 0, 0],
#     [0, 1, 1, 0, 1, 0, 1],
#     [1, 1, 1, 0, 1, 0, 1],
#     [0, 0, 0, 0, 1, 1, 1],
#     [0, 1, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 0, 0, 0],
# ]

answer = []
checked = [[0]*(n+1) for _ in range(n+1)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0


def dfs(i, j):
    global cnt
    mat[i][j] = '0'
    cnt += 1
    for d in range(4):
        x = i + dx[d]
        y = j + dy[d]

        if x < 0 or y < 0 or x >= n or y >= n:
            continue
        if mat[x][y] == '1':
            dfs(x, y)


for i in range(n):
    for j in range(n):
        if mat[i][j] == '1':
            cnt = 0
            dfs(i, j)
            answer.append(cnt)

print(len(answer))
answer.sort()
for a in answer:
    print(a)
