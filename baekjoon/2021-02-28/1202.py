# 보석 도둑
# https://www.acmicpc.net/problem/1202
import heapq
n, k = map(int, input().split())
jews = []
bags = []

for _ in range(n):
    jews.append(list(map(int, input().split())))
# jews.sort(key=lambda x: x[0])
for _ in range(k):
    bags.append(int(input()))
bags.sort()
# print(jews)
result = 0
temp = []
for bag in bags:
    while jews and bag >= jews[0][0]:
        heapq.heappush(temp, -heapq.heappop(jews)[1])
    if temp:
        result -= heapq.heappop(temp)
    elif not jews:
        break

print(result)
