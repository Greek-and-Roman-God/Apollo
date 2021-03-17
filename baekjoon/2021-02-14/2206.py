# 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206
from collections import deque
n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, list(input()))))

queue = deque()
queue.append([0, 0, 0])
miro = [[0]*m for _ in range(n)]
miro[0][0] = 1
while queue:
    loc = queue.popleft()
    x = loc[0]
    y = loc[1]
    wall = loc[2]
    for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        dx = move[0] + x
        dy = move[1] + y
        if not(0 <= dx < n and 0 <= dy < m):
            continue
        if miro[dx][dy] == 0:
            if mat[dx][dy] == 0:
                miro[dx][dy] = miro[x][y] + 1
            elif mat[dx][dy] > miro[x][y] + 1:
                miro[dx][dy] = miro[x][y] + 1
            queue.append([dx, dy, wall])
        if mat[dx][dy] == 1 and wall == 0:
            miro[dx][dy] = miro[x][y] + 1
            queue.append([dx, dy, 1])
for m in miro:
    print(str(m))
if miro[-1][-1] == 0:
    print(-1)
else:
    print(miro[-1][-1])
