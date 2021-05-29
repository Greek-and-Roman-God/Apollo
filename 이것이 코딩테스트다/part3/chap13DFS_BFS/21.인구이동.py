# 인구이동
# https://www.acmicpc.net/problem/16234
from collections import deque


n, l, r = map(int, input().split())
land = []
for _ in range(n):
    land.append(list(map(int, input().split())))

result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_unit(x, y, index):
    unit = []
    unit.append((x, y))

    q = deque()
    q.append((x, y))
    visited[x][y] = index
    summary = land[x][y]
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if l <= abs(land[x][y] - land[nx][ny]) <= r:
                    q.append((nx, ny))
                    visited[nx][ny] = index
                    summary += land[nx][ny]
                    cnt += 1
                    unit.append((nx, ny))

    for i, j in unit:
        land[i][j] = summary // cnt


while True:
    visited = [[-1]*n for i in range(n)]
    index = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                check_unit(i, j, index)
                index += 1
    if index == n*n:
        break
    result += 1
print(result)
