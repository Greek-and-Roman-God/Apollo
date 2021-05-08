# 특정 거리의 도시 찾기
from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

answer = []
distance = [-1] * (n+1)


queue = deque([x])
distance[x] = 0
while queue:
    q = queue.popleft()
    for node in graph[q]:
        if distance[node] == -1:
            distance[node] = distance[q] + 1
            queue.append(node)
            # print(distance[node])
            if distance[node] == k:
                answer.append(node)


if answer:
    answer.sort()
    for a in answer:
        print(a)
else:
    print(-1)
