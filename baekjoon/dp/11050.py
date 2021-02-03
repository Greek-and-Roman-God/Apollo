# 11050 이항계수1
# https://www.acmicpc.net/problem/11050
n, k = map(int, input().split())

dp = [[1]*(n+1) for i in range(n+1)]

dp[1][1] = 1
for i in range(2, n+1):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

# for d in dp:
#     print(d)
print(dp[n][k])
