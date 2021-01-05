# 11726 2xn 타일링
# https://www.acmicpc.net/problem/11726

def tile():
    n = int(input())
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for num in range(3, n+1):
        dp[num] = dp[num-1] + dp[num-2]
    return dp[n]


# print(tile() % 10007)

#
n = int(input())
dp = [0] * (n+2)
dp[1] = 1
dp[2] = 2
for num in range(3, n+1):
    dp[num] = dp[num-1] + dp[num-2]
    dp[num] %= 10007
print(dp[n])
