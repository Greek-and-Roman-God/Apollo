# 타임머신
# https://www.acmicpc.net/problem/11657
import sys
from collections import defaultdict

INF = int(1e9)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

routes = [INF]*(n+1)
routes[1] = 0
for i in range(1, n):
    for j in range(1, n+1):
        for c, b in graph[j]:
            if routes[j] == INF:
                continue
            if routes[b] > c + routes[j]:
                routes[b] = c + routes[j]

for j in range(1, n + 1):
    for c, b in graph[j]:
        if routes[j] == INF:
            continue
        if routes[b] > routes[j] + c:
            print(-1)
            sys.exit()

for i in range(2, n+1):
    if routes[i] == INF:
        print(-1)
    else:
        print(routes[i])
