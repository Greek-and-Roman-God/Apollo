# 2133 타일 채우기
# https://www.acmicpc.net/problem/2133

# 직전과는 2칸이 차이나니까 2칸일 때의 경우의 수인 3을 곱해주고
# 나머지 경우는 각 칸마다 생기는 특별한 경우의 수인 2를 곱해준다.
# 2안 경우를 제외하고 모든 상황에서 특별한 경우가 생기기 때문에 2를 제외한 모든 경우에 곱해주는 것

n = int(input())

dp = [0] * (n+2)
dp[2] = 3
for i in range(4, n+1, 2):
    for j in range(2, i, 2):
        if j == i-2:
            dp[i] += dp[j] * 3
        else:
            dp[i] += dp[j] * 2
    dp[i] += 2


print(dp[n])
