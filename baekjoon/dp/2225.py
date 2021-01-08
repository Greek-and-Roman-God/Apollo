# 2225 합분해
# https://mygumi.tistory.com/
# https://www.acmicpc.net/problem/2225

n, k = map(int, input().split())

dp = [[], [0]*(n+1)]

for i in range(n+1):
    dp[1][i] = 1

for i in range(2, k+1):
    temp = [0] * (n+1)
    for j in range(n+1):
        for l in range(j+1):
            temp[j] += dp[i-1][l]
        temp[j] = temp[j] % 1000000000
    dp.append(temp)
print(dp[k][n])
# print(dp)
# 조건에 맞는 dp를 만들어 놓고 실행하면 더 빠를지도
