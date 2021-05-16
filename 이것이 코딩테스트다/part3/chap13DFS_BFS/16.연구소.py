# 연구소
# https://www.acmicpc.net/problem/14502
from itertools import permutations
from copy import deepcopy
import sys
input = sys.stdin.readline


# def check(lab, virus):
#     vi_x, vi_y = virus
#     # for l in lab:
#     #     print(l)
#     for nx, ny in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#         x = vi_x + nx
#         y = vi_y + ny

#         if 0 <= x < len(lab) and 0 <= y < len(lab[0]) and lab[x][y] == 0:
#             lab[x][y] = 2
#             # empty.remove((x, y))
#             check(lab, (x, y))
#     return lab


# n, m = map(int, input().split())
# lab = []
# virus = []
# # walls = []
# empty = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     lab.append(row)

#     for j in range(m):
#         if row[j] == 2:
#             virus.append((i, j))
#         # elif row[j] == 1:
#         #     walls.append((i, j))
#         elif row[j] == 0:
#             empty.append((i, j))

# set_walls = list(permutations(empty, 3))
# # print(set_walls)

# result = -1

# for set_wall in set_walls:
#     temp_lab = deepcopy(lab)
#     # temp_empty = deepcopy(empty)

#     safe = 0
#     for x, y in set_wall:
#         temp_lab[x][y] = 1

#     for vi in virus:
#         temp_lab = check(temp_lab, vi)

#     # result.append(len(temp_empty))
#     for row in temp_lab:
#         for r in row:
#             if r == 0:
#                 safe += 1
#                 # print(max(result))
#     result = max(result, safe)

# print(result)


# 2 ===================================================


n, m = map(int, input().split())
lab = []
virus = []
# walls = []
empty = []
for i in range(n):
    row = list(map(int, input().split()))
    lab.append(row)

    for j in range(m):
        if row[j] == 2:
            virus.append((i, j))
        # elif row[j] == 1:
        #     walls.append((i, j))
        elif row[j] == 0:
            empty.append((i, j))

# set_walls = list(permutations(empty, 3))
# print(set_walls)

empty_cnt = len(empty) - 3

result = -1

# for set_wall in set_walls:
# print(temp_lab)
# for wall_x, wall_y in set_wall:
#     temp_lab[wall_x][wall_y] = 1


def dfs(lab, wall_cnt):
    global result
    # print(wall_cnt)
    if wall_cnt == 3:
        result = max(bfs(lab), result)
        return

    for i in range(len(lab)):
        for j in range(len(lab[0])):
            # print("?")
            if lab[i][j] == 0:
                # print("왜 안돼")
                lab[i][j] = 1
                dfs(lab, wall_cnt + 1)
                lab[i][j] = 0


def bfs(lab):
    temp_virus = deepcopy(virus)
    # temp_empty = empty_cnt
    while temp_virus:
        vi_x, vi_y = temp_virus.pop(0)

        for nx, ny in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            x = vi_x + nx
            y = vi_y + ny

            if 0 <= x < len(lab) and 0 <= y < len(lab[0]) and lab[x][y] == 0:
                lab[x][y] = 2
                temp_virus.append((x, y))

    safe = 0
    for i in range(n):
        # print(lab[i])
        for j in range(m):
            if lab[i][j] == 0:
                safe += 1
            elif lab[i][j] == 2 and (i, j) not in virus:
                lab[i][j] = 0
    # print("=======================")
    return safe


dfs(lab, 0)

print(result)

# deepcopy보다 slicing의 시간복잡도가 더 빠르다. slicing은 요소 갯수만큼의 시간복잡도를 가지기 때문에 copy 모듈의 연산을 수행하는 것보다 시간이 적게 소요될 수 있다.
# deepcopy는 객체의 모든 속성과 데이터를 복사한다. 떄문에 배열보다는 class 객체나, dictionary 같은 해쉬값을 복사할 때 이점이 있다.
# 때문에 객체 등을 복사할 때는 복사 메서드를 커스텀으로 만들어서 사용한다고 한다.
