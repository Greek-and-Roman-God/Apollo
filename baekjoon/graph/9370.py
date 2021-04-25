# 미확인 도착지
import sys
import heapq


input = sys.stdin.readline
INF = int(1e9)

t = int(input().strip())
for _ in range(t):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    if g > h:
        g, h = h, g

    for _ in range(m):
        a, b, d = map(int, input().split())
        if a > b:
            a, b = b, a
        if [a, b] == [g, h]:
            graph[a].append((b, 1))
            graph[b].append((a, 1))
        else:
            graph[a].append((b, 2))
            graph[b].append((a, 2))

    end = []

    for _ in range(t):
        end.append(int(input().strip()))

    def dijkstra(start):
        q = []
        distance = [INF] * (n+1)
        # print(distance, start)
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue

            for node, weight in graph[now]:
                cost = dist + weight
                if cost < distance[node]:
                    distance[node] = cost
                    heapq.heappush(q, (cost, node))
        return distance
    start = dijkstra(s)
    pass1 = dijkstra(g)
    pass2 = dijkstra(h)
    possible = []
    for e in end:
        dist = min(start[g] + pass1[h] + pass2[e],
                   start[h] + pass2[g] + pass1[e])
        print(dist, e)
        if dist == start[e]:
            possible.append(e)
    possible.sort()
    for p in possible:
        print(p, end=" ")
    print()

    # answer = []
    # for e in end:
    #     if start[e] // 2:
    #         answer.append(e)

    # print(answer)
