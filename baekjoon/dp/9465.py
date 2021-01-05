# 9465 스티커
# https://www.acmicpc.net/problem/9465


t = int(input())
for _ in range(t):
    n = int(input())
    stickers = []
    for _ in range(2):
        row = list(map(int, input().split()))
        stickers.append(row)

    dp = [[0]*(n+1), [0]*(n+1)]
    dp[0][1] = stickers[0][0]
    dp[1][1] = stickers[1][0]

    for i in range(2, n+1):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + stickers[0][i-1]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + stickers[1][i-1]
    print(max(dp[0][n], dp[1][n]))
