# 2636 치즈
# https://www.acmicpc.net/problem/2636
from collections import deque
# m, n = map(int, input().split())
# mat = []
# cheese = []
# for i in range(m):
#     row = input().split()
#     mat.append(row)
#     for j in range(n):
#         if row[j] == 1:
#             cheese.append([i, j])

m, n = [13, 12]
mat = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
for i in range(m):
    for j in range(n):
        if i == 0 or i == m-1 or j == 0 or j == n-1:
            mat[i][j] = -1
queue = deque()
check = [[0]*n for _ in range(m)]
print(mat)


def dfs(i, j):

    if mat[i][j] == 1:
        queue.append([i, j])


for i in range(m):
    for j in range(n):
        if mat[i][j] == -1:
            dfs(i, j)
