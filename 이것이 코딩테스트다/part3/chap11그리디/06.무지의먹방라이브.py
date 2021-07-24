# 무지의 먹방 라이브
import heapq
from collections import deque


def solution(food_times, k):
    answer = 0
    queue = deque()
    for i, food in enumerate(food_times):
        queue.append([food, i+1])

    while k and queue:
        print(queue)
        food = queue.popleft()
        food[0] -= 1
        if food[0] != 0:
            queue.append(food)
        k -= 1
    print(queue)
    answer = queue.pop()
    return answer[1]


answer = solution([3, 1, 2], 5)
print(answer)

# 2021-07-25


def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    q = []

    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    sum_time = 0
    previous = 0
    length = len(food_times)

    while sum_time + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_time += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])

    return result[(k-sum_time) % length][1]
