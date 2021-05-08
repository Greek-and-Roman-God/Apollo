# KCM Travel
# https://www.acmicpc.net/problem/10217
import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(k):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))

    dp = [[INF] * (m+1) for _ in range(n+1)]
    dp[1][0] = 0

    for money in range(m+1):
        for now in range(1, n+1):
            if dp[now][money] == INF:
                continue
            now_dist = dp[now][money]
            for next_port, next_m, next_d in graph[now]:
                if money + next_m > m:
                    continue

                dp[next_port][money +
                              next_m] = min(dp[next_port][money+next_m], now_dist + next_d)
    result = min(dp[n])
    if result != INF:
        print(result)
    else:
        print("Poor KCM")
