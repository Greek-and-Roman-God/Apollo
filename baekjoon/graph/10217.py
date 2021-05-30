# KCM Travel
# https://www.acmicpc.net/problem/10217
# 소요시간은 짧지만 비용이 비싼 경우와 소요시간은 길지만 비용이 싼 경우를 모두 탐색해야한다.
# 소요시간이 짧은 경로를 탐색하는 다익스트라만 사용할 경우 원하는 결과를 얻지 못할 수 있다.
# 그래서 사용하는 것이 DP

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

    # 주어진 정점 * 총 지원 비용 크기의 배열을 생성하고 INF로 초기화
    # 모든 정점에 대해 총 지원 비용 이내에 해당하는 모든 금액으로 탐색을 진행한다는 의미
    dp = [[INF] * (m+1) for _ in range(n+1)]
    dp[1][0] = 0    # 출발지점 1번공항, 1번 공항에 대한 비용은 0원

    for money in range(m+1):
        for now in range(1, n+1):
            if dp[now][money] == INF:
                continue
            now_dist = dp[now][money]
            for next_port, next_m, next_d in graph[now]:
                if money + next_m > m:
                    continue

                # next_port 공항의 money + next_m의 비용으로 갈 수 있는 시간을 최소로 업데이트
                dp[next_port][money + next_m] =\
                    min(dp[next_port][money+next_m], now_dist + next_d)
    # n공항에 저장된 소요시간 중 가장 빠른 시간을 선택
    result = min(dp[n])
    if result != INF:
        print(result)
    else:
        print("Poor KCM")
