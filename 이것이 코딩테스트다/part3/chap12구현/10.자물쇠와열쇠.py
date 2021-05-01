# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059
import copy


def rotated(a):
    n = len(a)
    m = len(a[0])

    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result


def insert_key(x, y, temp, key):
    m = len(key)
    for i in range(x, x + m):
        for j in range(y, y + m):
            temp[i][j] += key[i-x][j-y]

    return temp


def check(m, n, result):
    # for r in result:
    #     print(r)
    # print("-------------------------------")
    for i in range(n):
        for j in range(n):
            # print(n, i, j)
            item = result[i+(m-1)][j+(m-1)]
            # print(item)
            if item == 0 or item == 2:
                return False
    return True


def solution(key, lock):
    # answer = []
    n = len(lock)
    m = len(key)
    temp = [[0] * (n + 2*(m-1)) for _ in range(n + 2*(m-1))]

    for i in range(n):
        for j in range(n):
            # print(i, j)
            temp[i+(m-1)][j+(m-1)] = lock[i][j]

    for x in range(n + (m-1)):
        for y in range(n + (m-1)):
            for _ in range(4):
                key = rotated(key)
                plate = copy.deepcopy(temp)
                result = insert_key(x, y, plate, key)
                if check(m, n, result):
                    return True

    return False


# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
#                [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

print(solution([[1, 0], [0, 1]],
               [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))


# print(solution([[0, 0], [0, 0]],
#                [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
