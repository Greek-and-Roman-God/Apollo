# 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866
from collections import deque
n, k = map(int, input().split())
person = deque()
for i in range(1, n+1):
    person.append(i)
result = []
for _ in range(n):
    i = 1
    while i < k:
        person.append(person.popleft())
        i += 1
    result.append(str(person.popleft()))
print('<'+', '.join(result)+'>')
