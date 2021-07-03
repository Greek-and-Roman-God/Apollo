# 화성탐사
import heapq
INF = int(10e9)

for _ in range(int(input())):
    n = int(input())
    graph = []

    for _ in range(n):
        graph.append(map(int, input().split()))
    distance = [[INF]*n for _ in range(n)]

    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]

                if cost < dist[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    print(distance[-1][-1])
