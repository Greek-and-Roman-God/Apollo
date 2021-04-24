# 최단 경로
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


v, e = map(int, input().split())
k = int(input().strip())

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])


q = []
heapq.heappush(q, (0, k))
distance[k] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for node, weight in graph[now]:
        cost = dist + weight
        if cost < distance[node]:
            distance[node] = cost
            heapq.heappush(q, (cost, node))


for i in distance[1:]:
    # print(i, end=" ")
    if i == INF:
        print("INF")
    else:
        print(i)
