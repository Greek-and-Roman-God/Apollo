# rgb거리
# https://www.acmicpc.net/problem/1149
n = int(input())
costs = []
for _ in range(n):
    costs.append(list(map(int, input().split())))

dp = [[0]*3 for _ in range(n)]
dp[0] = costs[0]

for i in range(1, n):
    for j in range(3):
        min_cost = 1001*n
        for k in range(3):
            if k != j and min_cost > dp[i-1][k]:
                min_cost = dp[i-1][k]
        dp[i][j] = min_cost + costs[i][j]
print(min(dp[n-1]))

# 최숫값의 초기값을 잘못 설정했었음
# 한가지 색으로 집을 페인팅하는데 드는 비용은 최대 1000으로 주어져있으므로
# dp의 최소값을 가져와서 비교하는 min_cost의 값은 총 비용의 최댓값인 1000*n보다 커야함
