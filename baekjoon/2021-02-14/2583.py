# 영역 구하기
# https://www.acmicpc.net/problem/2583
from collections import deque
m, n, k = map(int, input().split())

mat = [[0]*n for _ in range(m)]
for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())

    for x in range(sy, ey):
        for y in range(sx, ex):
            mat[x][y] = 1
    # for m in mat:
    #     print(m)


queue = deque()


def bfs(i, j):
    queue.append([i, j])
    area = 1
    while queue:
        loc = queue.popleft()
        mat[i][j] = 1
        dx = loc[0]
        dy = loc[1]

        for mov in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x = mov[0] + dx
            y = mov[1] + dy

            if not (0 <= x < m and 0 <= y < n):
                continue

            if mat[x][y] == 0:
                mat[x][y] = 1
                area += 1
                queue.append([x, y])
    return area


# for ma in mat:
#     print(ma)


areas = []
for i in range(m):
    for j in range(n):
        if mat[i][j] == 0:
            areas.append(bfs(i, j))
print(len(areas))
print(' '.join(list(map(str, sorted(areas)))))
