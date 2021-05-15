# 카드 정렬하기
# https://www.acmicpc.net/problem/1715
import heapq

n = int(input())
nums = []
for _ in range(n):
    heapq.heappush(nums, int(input()))
answer = 0
while len(nums) > 1:
    cnt = heapq.heappop(nums) + heapq.heappop(nums)
    answer += cnt
    heapq.heappush(nums, cnt)
print(answer)
