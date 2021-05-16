# 경쟁적 감염
# https://www.acmicpc.net/problem/18405
import heapq
from collections import deque
n, k = map(int, input().split())

plate = []
virus = []
for i in range(n):
    row = list(map(int, input().split()))
    plate.append(row)
    for j in range(n):
        if row[j] != 0:
            heapq.heappush(virus, (0, row[j], i, j))

s, x, y = map(int, input().split())
# print(virus)

while virus:
    sec, v_type, v_x, v_y = heapq.heappop(virus)
    if sec == s:
        break
    for nx, ny in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_x = nx + v_x
        next_y = ny + v_y
        if 0 <= next_x < n and 0 <= next_y < n and plate[next_x][next_y] == 0:
            plate[next_x][next_y] = v_type
            heapq.heappush(virus, (sec + 1, v_type, next_x, next_y))


# for i in plate:
#     print(i)
print(plate[x-1][y-1])


n, k = map(int, input().split())

plate = []
virus = []
for i in range(n):
    plate.append(list(map(int, input().split())))
    for j in range(n):
        if plate[i][j] != 0:
            virus.append((plate[i][j], 0, i, j))

virus.sort()
s, x, y = map(int, input().split())
# print(virus)

virus = deque(virus)

while virus:
    v_type, sec, v_x, v_y = virus.popleft()
    if sec == s:
        break
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_x = dx + v_x
        next_y = dy + v_y
        if 0 <= next_x < n and 0 <= next_y < n and plate[next_x][next_y] == 0:
            plate[next_x][next_y] = v_type
            virus.append((v_type, sec+1, next_x, next_y))


# for i in plate:
#     print(i)
print(plate[x-1][y-1])
