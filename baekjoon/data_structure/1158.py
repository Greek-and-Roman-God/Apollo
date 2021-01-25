# 1158 요세푸스 문제
# https://www.acmicpc.net/problem/1158

from collections import deque
# 시간초과
# n, k = map(int, input().split())
# queue = [str(num) for num in range(1, n+1)]
# result = []
# # print(queue)
# i = 1
# while len(queue) != 1:
#     temp = queue.pop(0)
#     if i % k:
#         queue.append(temp)
#     else:
#         result.append(temp)
#     i += 1
# else:
#     result.append(queue[0])
# print('<'+', '.join(result)+'>')


# 덱
# queue는 멀티스레드를 위한 모듈이기 떄문에 단일 스레드에 쓰기에는 비효율적입니다.
n, k = map(int, input().split())
deque = deque()
for i in range(n):
    deque.append(str(i+1))
result = []

while deque:
    for _ in range(k-1):
        deque.append(deque.popleft())
    result.append(deque.popleft())
print('<'+', '.join(result)+'>')
