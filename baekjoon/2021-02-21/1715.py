# 카드 정렬하기
# https://www.acmicpc.net/problem/1715
import heapq

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

hap = 0
while len(heap) != 1:
    cnt = heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap, cnt)
    hap += cnt
print(hap)
