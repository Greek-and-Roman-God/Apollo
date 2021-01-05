# 9095 1,2,3 더하기
# https://www.acmicpc.net/problem/9095

n = int(input())

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4
for num in range(4, 12):
    dp[num] = dp[num-1] + dp[num-2] + dp[num-3]


for _ in range(n):
    case = int(input())
    print(dp[case])
