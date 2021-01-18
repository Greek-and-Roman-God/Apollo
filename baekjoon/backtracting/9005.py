# 9005 1,2,3 더하기
# https://www.acmicpc.net/problem/9095

# dp
t = int(input())
for _ in range(t):
    n = int(input())

    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for n in range(3, n+1):
        dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
    print(dp[n])

# 백트래킹
t = int(input())
for _ in range(t):
    n = int(input())
    answer = 0

    def dfs(sum):
        global answer
        if sum > n:
            return
        if sum == n:
            answer += 1

        dfs(sum+1)
        dfs(sum+2)
        dfs(sum+3)

    dfs(0)
    print(answer)
