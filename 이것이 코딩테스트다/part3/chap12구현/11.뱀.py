# 뱀
from collections import deque
# n = int(input())
# k = int(input())

# mat = [[0] * (n+1) for _ in range(n+1)]

# for _ in range(k):
#     x, y = map(int, input().split())
#     mat[x][y] = 2

# l = int(input())
# direction = deque()

# for _ in range(l):
#     x, c = input().split()
#     direction.append([int(x), c])

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# snake = deque([(1, 1)])    # 처음 위치는 1,1
# # x, y = 0, 1  # 처음 방향은 오른쪽
# d_idx = 0


# def turn(d_idx, c):
#     if c == "D":
#         return (d_idx + 1) % 4
#     else:
#         return (d_idx - 1) % 4


# # for m in mat:
# #     print(m)
# sec = 0
# while True:
#     # print(f'sec = {sec+1}==========================')
#     # print(f'snake = {snake}')
#     # print(f'direction = {direction}')
#     x = snake[-1][0] + dx[d_idx]
#     y = snake[-1][1] + dy[d_idx]
#     # print(f'x = {x}, y = {y}')
#     if 1 <= x <= n and 1 <= y <= n and (x, y) not in snake:    # 벽이나 몸에 부딪히지 않음
#         if mat[x][y] == 2:
#             mat[x][y] = 0
#         else:
#             snake.popleft()
#         snake.append((x, y))
#         sec += 1
#     else:
#         print(sec+1)
#         break

#     if direction and direction[0][0] == sec:
#         _, direct = direction.popleft()
#         d_idx = turn(d_idx, direct)
#         # print(f'd_idx = {d_idx}로 변경 *****************')

# 2021-08-20

# 보드의 크기 n x n
# 뱀의 위치 (0,0)
# 뱀의 길이 1
# 진행 방향 오른쪽

# 진행 방향으로 한칸씩 늘림
# 늘린 칸에 사과가 있으면 꼬리를 안 없앰
# 늘린 칸에 사과가 없으면 꼬리를 없앰

# 뱀은 queue로 구현 / 머리로 들어가서 꼬리로 나오는 형태
# 오른쪽  D -> 시계방향
# 왼쪽    L -> 반시계방향

n = int(input())
k = int(input())

game_map = [[0] * n for _ in range(n)]

rotate = [[0, 1], [1, 0], [0, -1], [-1, 0]]

snake = deque([(0,0)])
heading = 0

for _ in range(k):
    x, y = map(int, input().split())
    game_map[x-1][y-1] = 1

l = int(input())
move = []
for _ in range(l):
    sec, direct = input().split()
    move.append((int(sec), direct))

sec = 1
while(True):
    direct = rotate[heading]
    x, y = snake[-1][0] + direct[0], snake[-1][1] + direct[1]
    print(sec, x+1,y+1,snake)
    if 0 <= x < n and 0 <= y < n and (x, y) not in snake:
        snake.append((x, y))
    else:
        break

    if game_map[x][y] == 0:
        snake.popleft()
    else:
        game_map[x][y] = 0

    if move and move[0][0] == sec:
        print(move[0])
        if move[0][1] == "D":
            heading = (heading + 1) % 4
        else:
            heading = (heading - 1) % 4
        move.pop(0)

    sec += 1

print(sec)