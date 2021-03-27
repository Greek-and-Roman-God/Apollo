# 미로탈출
n, m = map(int, input().split())
miro = []

for _ in range(n):
    miro.append(list(map(int, list(input()))))


def path(i, j):
    queue = [(i, j)]

    while queue:
        temp = queue.pop(0)
        for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x = move[0] + temp[0]
            y = move[1] + temp[1]
            if 0 <= x < n and 0 <= y < m and miro[x][y] == 1:
                miro[x][y] = miro[temp[0]][temp[1]] + 1
                queue.append((x, y))


path(0, 0)
print(miro[n-1][m-1])
