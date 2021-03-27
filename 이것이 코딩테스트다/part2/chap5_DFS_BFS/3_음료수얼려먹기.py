# 음료수 얼려먹기
n, m = map(int, input().split())
ice = []
for _ in range(n):
    ice.append(list(map(int, list(input()))))
chk = [[0]*m for _ in range(n)]


def check(i, j):
    queue = [(i, j)]
    while queue:
        temp = queue.pop(0)
        for move in [(1, 0), (0, 1)]:
            x = move[0] + temp[0]
            y = move[1] + temp[1]

            if 0 <= x < n and 0 <= y < m and ice[x][y] == 0:
                ice[x][y] = 1
                queue.append((x, y))


result = 0
for i in range(n):
    for j in range(m):
        if ice[i][j] == 0:
            check(i, j)
            ice[i][j] = 1
            result += 1
print(result)
