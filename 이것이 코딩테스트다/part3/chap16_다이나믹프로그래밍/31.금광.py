# 금광
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    golds = list(map(int, input().split()))

    dp = []
    for i in range(n):
        dp.append(golds[i*m:i*m+m])
    # print(dp)
    result = -1
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp[i][j] += max(dp[i][j-1], dp[i+1][j-1])
            elif i == n-1:
                dp[i][j] += max(dp[i][j-1], dp[i-1][j-1])
            else:
                dp[i][j] += max(dp[i][j-1], dp[i+1][j-1], dp[i-1][j-1])
            result = max(result, dp[i][j])
    # print(dp)
    print(result)
