# 효율적인 화폐 구성
n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [10001] * (m+1)
dp[0] = 0

for i in range(1, m+1):
    for coin in coins:
        if i-coin >= 0:
            dp[i] = min(dp[i], dp[i-coin]+1)
print(dp[m] if dp[m] == 10001 else -1)
