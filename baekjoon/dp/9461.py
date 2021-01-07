# 9461 파도반 수열
# https://www.acmicpc.net/problem/9461

import sys
n = int(input())
dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, 101):
    dp[i] = dp[i-2] + dp[i-3]


for _ in range(n):
    print(dp[int(input())])


# 다른 사람 풀이
input = sys.stdin.readline


T = int(input())
for test in range(T):
    n = int(input())

    cache = [0] * (n+1)

    def P(n):
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif n == 3:
            return 1

        if cache[n]:
            return cache[n]

        cache[n] = P(n-2) + P(n-3)
        return cache[n]

    print(P(n))
