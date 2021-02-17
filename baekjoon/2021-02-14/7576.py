# 토마토
# https://www.acmicpc.net/problem/7576
from collections import deque
m, n = map(int, input().split())
box = []
queue = deque()
cnt = 0
for i in range(n):
    row = list(map(int, input().split()))
    box.append(row)

    for j in range(m):
        if row[j] == 1:
            queue.append([i, j])

while queue:
    loc = queue.popleft()
    x = loc[0]
    y = loc[1]

    for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        dx = move[0] + x
        dy = move[1] + y

        if not (0 <= dx < n and 0 <= dy < m):
            continue

        if box[dx][dy] == 0:
            box[dx][dy] = box[x][y] + 1
            queue.append([dx, dy])
            cnt = box[x][y]
for p in box:
    if 0 in p:
        print(-1)
        break
else:
    print(cnt)
