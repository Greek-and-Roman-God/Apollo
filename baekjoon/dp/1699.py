# 1699 제곱수의 합
# https://www.acmicpc.net/problem/1699

# 시간 초과
# n = int(input())

# dp = [0] * (n+1)
# dp[1] = 1

# for i in range(2, n+1):
#     temp = []
#     if i**0.5 == int(i**0.5):
#         temp.append(1)
#     for num in range(1, i//2+1):
#         temp.append(dp[num]+dp[i-num])
#     print(temp)
#     dp[i] = min(temp)
# print(dp[n])


# 2
# dp[n] = dp[n-1]+1 중 최솟값을 구함
# 어떤 수가 최숫값이 될지 모르기 때문에 제곱수를 빼서 직전의 dp값을 확인해 최솟값을 찾는다.
n = int(input())

dp = [0] * (n+1)

for i in range(1, n+1):
    j = 1

    while j**2 <= i:
        if dp[i] > dp[i-j**2]+1 or dp[i] == 0:
            dp[i] = dp[i-j**2] + 1
        j += 1
print(dp)
