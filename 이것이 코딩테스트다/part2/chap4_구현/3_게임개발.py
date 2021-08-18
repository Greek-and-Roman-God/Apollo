# 게임개발

direction = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
]

n, m = map(int, input().split())
pos_x, pos_y, direct = map(int, input().split())

mat = [[0]*m for _ in range(n)]
mat[pos_x][pos_y] = 1
map_list = []
for _ in range(n):
    map_list.append(list(map(int, input().split())))

cnt = 0
while True:

    direct += 1  # 왼쪽으로 회전

    dx = pos_x + direction[direct % 4][0]
    dy = pos_y + direction[direct % 4][1]

    cnt += 1

    if 0 <= dx < n and 0 <= dy < m and map_list[dx][dy] == 0 and mat[dx][dy] == 0:
        mat[dx][dy] = 1
        pos_x = dx
        pos_y = dy
        cnt = 0

    if cnt == 4:
        temp_x = pos_x - direction[direct % 4][0]
        temp_y = pos_y - direction[direct % 4][1]
        if 0 <= temp_x < n and 0 <= temp_y < m and map_list[dx][dy] == 0 and mat[dx][dy] == 0:
            pos_x = temp_x
            pos_y = temp_y
            cnt = 0
        else:
            break
result = 0
for row in mat:
    result += row.count(1)
print(result)

# 2021-08-18

rotate = [(-1, 0), (0, -1), (1, 0), (0, 1)]

m, n = map(int, input().split())
loc_x, loc_y, dir_idx = map(int, input().split())
island = [list(map(int, input().split())) for _ in range(m)]
island[loc_x][loc_y] = 2

cnt = 0
result = 1
while True:
    nx, ny = loc_x+rotate[dir_idx][0], loc_y+rotate[dir_idx][1]
    # print(loc_x, loc_y, dir_idx, "/", nx, ny)
    # for i in island:
    #     print(i)
    if island[nx][ny] != 0:
        dir_idx = (dir_idx+1) % 4
        cnt += 1
    else:
        cnt = 0
        loc_x, loc_y = nx, ny
        island[nx][ny] = 2
        result += 1

    if cnt == 4:
        nx, ny = loc_x-rotate[dir_idx][0], loc_y-rotate[dir_idx][1]
        if island[nx][ny] != 1:
            loc_x, loc_y = nx, ny
        else:
            break
        cnt = 0
    # print("=========================")

print(result)
