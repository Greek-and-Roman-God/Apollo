# 2193 이친수
# https://www.acmicpc.net/problem/2193

n = int(input())
dp = [0] * (n+2)
dp[1] = 1
dp[2] = 1


for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])
