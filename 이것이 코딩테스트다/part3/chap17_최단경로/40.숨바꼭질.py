# 숨바꼭질
import heapq

INF = int(10e9)

n, m = map(int, input().split())

start = 1

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = [(0, start)]
distance[start] = 0
while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))
distance = distance[1:]
print(distance)
max_dist = max(distance)
hide = distance.index(max_dist) + 1
cnt = distance.count(max_dist)
print(hide, max_dist, cnt)
