# 11057 오르막 수
# https://www.acmicpc.net/problem/11057
n = int(input())

dp = [[], [0]*10]

for num in range(10):
    dp[1][num] = 1

for i in range(2, n+1):
    temp = [0] * 10
    for j in range(10):
        for k in range(j, 10):
            # print(i, j, k)
            temp[k] += dp[i-1][j]
    dp.append(temp)
print(sum(dp[n]) % 10007)
