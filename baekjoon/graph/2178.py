# 미로탐색
# https://www.acmicpc.net/problem/2178
from collections import deque


n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, list(input()))))

queue = deque()
queue.append((0, 0))

while queue:
    pos_x, pos_y = queue.popleft()

    for move in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        x = move[0] + pos_x
        y = move[1] + pos_y
        if not (0 <= x < n and 0 <= y < m):
            continue
        if mat[x][y] == 1:
            mat[x][y] = mat[pos_x][pos_y] + 1
            queue.append((x, y))

print(mat[n-1][m-1])
