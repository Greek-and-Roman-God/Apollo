# 10844 쉬운 계단 수
# https://www.acmicpc.net/problem/10844

n = int(input())

dp = [[], [0] * 10]


for j in range(1, 10):
    dp[1][j] = 1

for i in range(2, n+1):
    temp = [0] * 10
    for j in range(0, 10):
        # print(i, j)
        if j == 0:
            temp[j] = dp[i-1][j+1]
        elif j == 9:
            temp[j] = dp[i-1][j-1]
        else:
            temp[j] = dp[i-1][j+1] + dp[i-1][j-1]
    # print(temp)
    dp.append(temp)
print(sum(dp[n]) % 1000000000)
