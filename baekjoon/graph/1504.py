# 특정한 최단 경로
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
v1, v2 = map(int, input().split())


def dijkstra(start):
    q = []
    distance = [INF] * (v+1)
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


start_1 = dijkstra(1)
start_v1 = dijkstra(v1)
start_v2 = dijkstra(v2)
# print(distance1)
# print(distance2)
# print(distance1[1]+distance2[v]+distance1[v2])
# print(distance1[v]+distance2[1]+distance2[v1])
answer = min(start_1[v1] + start_v1[v2] + start_v2[v],
             start_1[v2] + start_v2[v1] + start_v1[v])

if answer >= INF:
    print(-1)
else:
    print(answer)
