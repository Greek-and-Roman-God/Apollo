# 가운데를 말해요
# https://www.acmicpc.net/problem/1655

import heapq
import sys
n = int(sys.stdin.readline())
max_heap = []
min_heap = []
for _ in range(n):
    number = int(sys.stdin.readline())

    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-number, number))
    else:
        heapq.heappush(min_heap, (number, number))

    if min_heap and max_heap[0][1] > min_heap[0][1]:
        max_value = heapq.heappop(max_heap)[1]
        min_value = heapq.heappop(min_heap)[1]
        heapq.heappush(min, (max_value, max_value))
        heapq.heappush(max, (-min_value, min_value))

    print(max_heap[0][1])
