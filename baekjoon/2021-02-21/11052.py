# 카드 구매하기
# https://www.acmicpc.net/problem/11052
n = int(input())
p = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(len(p)):
    dp[i] = p[i]

for i in range(2, n+1):

    for j in range(i-1, 0, -1):
        temp = i - j
        dp[i] = max(dp[i], dp[temp] + dp[j])
print(dp[n])
