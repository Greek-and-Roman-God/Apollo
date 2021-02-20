# 7569 토마토
# https://www.acmicpc.net/problem/7569
from collections import deque
import sys


def input():
    return sys.stdin.readline()


m, n, h = map(int, input().split())
box = []
queue = deque()
cnt = 0
for i in range(h):
    temp = []
    for j in range(n):
        row = list(map(int, input().split()))
        temp.append(row)

        for k in range(len(row)):
            if row[k] == 1:
                queue.append([i, j, k])

    box.append(temp)
# print(box)
# print(queue)

while queue:
    loc = queue.popleft()
    x = loc[0]
    y = loc[1]
    z = loc[2]

    for move in [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]:
        dx = move[0] + x
        dy = move[1] + y
        dz = move[2] + z
        if not (0 <= dx < h and 0 <= dy < n and 0 <= dz < m):
            continue
        # print(box[dx][dy][dz])
        if box[dx][dy][dz] == 0:
            box[dx][dy][dz] = box[x][y][z] + 1
            queue.append([dx, dy, dz])
            cnt = box[x][y][z]

for b in box:
    for toma in b:
        if 0 in toma:
            cnt = -1
            break

print(cnt)
