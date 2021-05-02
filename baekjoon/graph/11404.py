# 플로이드
# https://www.acmicpc.net/problem/11404
import sys
from collections import defaultdict

INF = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
# print(graph)

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=" ")
            continue
        print(graph[a][b], end=" ")
    print()
