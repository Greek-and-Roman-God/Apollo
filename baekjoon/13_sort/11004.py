# 11004 K번째 수
# https://www.acmicpc.net/problem/11004
n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
print(nums[k-1])
