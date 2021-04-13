# 1로 만들기
x = int(input())
dp = [0] * (x+1)
dp[1] = 0

for i in range(2, x+1):
    temp = []
    temp.append(dp[i-1])
    if i % 2 == 0:
        temp.append(dp[i//2])
    if i % 3 == 0:
        temp.append(dp[i//3])
    if i % 5 == 0:
        temp.append(dp[i//5])
    # print(i, temp)
    dp[i] = min(temp) + 1
print(dp[-1])
