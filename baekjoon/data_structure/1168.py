# 1168 요세푸스 문제 2
# https://suri78.tistory.com/113
from collections import deque
import sys


def input():
    return sys.stdin.readline().strip()


n, k = map(int, input().split())
deque = deque([str(num) for num in range(1, n+1)])
result = []

while deque:
    deque.rotate(-k+1)
    result.append(deque.popleft())
print('<'+', '.join(result)+'>')

# rotate() 인자가 음수일 경우 왼쪽으로 회전하며
# 양수가 주어지면 오른쪽으로 회전한다.
# list = deque([a,b,c])가 있을 때
# table.rotate(1)의 결과는 [c,a,b]
# table.rotate(-1)의 결과는 [b,c,a]
