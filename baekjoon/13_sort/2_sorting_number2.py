# 2751 수 정렬하기 2
# https://www.acmicpc.net/problem/2751
# 파이썬은 너무 느려서 pypy로 해야된다함
import heapq

n = int(input())
nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)


def heap_sort(a):
    heap = []
    for i in a:
        heapq.heappush(heap, i)
    for i in range(len(a)):
        print(heapq.heappop(heap))


heap_sort(nums)


# 2
# pypy로 돌리면 통과
n = int(input())
nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)

nums.sort()
for num in nums:
    print(num)
