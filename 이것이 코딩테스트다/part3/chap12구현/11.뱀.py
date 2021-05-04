# 뱀
from collections import deque
n = int(input())
k = int(input())

mat = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    x, y = map(int, input().split())
    mat[x][y] = 2

l = int(input())
direction = deque()

for _ in range(l):
    x, c = input().split()
    direction.append([int(x), c])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

snake = deque([(1, 1)])    # 처음 위치는 1,1
# x, y = 0, 1  # 처음 방향은 오른쪽
d_idx = 0


def turn(d_idx, c):
    if c == "D":
        return (d_idx + 1) % 4
    else:
        return (d_idx - 1) % 4


# for m in mat:
#     print(m)
sec = 0
while True:
    # print(f'sec = {sec+1}==========================')
    # print(f'snake = {snake}')
    # print(f'direction = {direction}')
    x = snake[-1][0] + dx[d_idx]
    y = snake[-1][1] + dy[d_idx]
    # print(f'x = {x}, y = {y}')
    if 1 <= x <= n and 1 <= y <= n and (x, y) not in snake:    # 벽이나 몸에 부딪히지 않음
        if mat[x][y] == 2:
            mat[x][y] = 0
        else:
            snake.popleft()
        snake.append((x, y))
        sec += 1
    else:
        print(sec+1)
        break

    if direction and direction[0][0] == sec:
        _, direct = direction.popleft()
        d_idx = turn(d_idx, direct)
        # print(f'd_idx = {d_idx}로 변경 *****************')
