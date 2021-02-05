# 1932 정수 삼각형
# https://www.acmicpc.net/problem/1932

n = int(input())
triangle = [[0]]
for _ in range(n):
    triangle.append(list(map(int, input().split())))

# dp = [0] * (n+1)
# dp[1] = triangle[1][0]

# for i in range(2, n+1):
#     temp = []
#     for j in range(len(triangle[i])):
#         temp.append(dp[])


dp = [[0]*n for n in range(1, len(triangle)+1)]
dp[0] = [triangle[0][0]]

for i in range(1, len(triangle)):

    for j, num in enumerate(triangle[i]):
        if j == 0:
            dp[i][j] = num + dp[i-1][j]
        elif j == len(triangle[i])-1:
            dp[i][j] = num + dp[i-1][len(triangle[i])-2]
        else:
            dp[i][j] = num + max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[-1]))
