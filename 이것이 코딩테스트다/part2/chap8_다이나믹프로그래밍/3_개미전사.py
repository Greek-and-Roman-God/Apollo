# 개미전사
n = int(input())
nums = list(map(int, input().split()))
dp = [0] * 101
dp[1] = nums[0]
dp[2] = max(nums[0], nums[1])

for i in range(3, n+1):
    dp[i] = max(dp[i-2], dp[i-3] + nums[i-1])
print(dp[n])
