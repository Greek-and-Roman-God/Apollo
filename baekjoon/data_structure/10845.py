# 10845 큐
# https://www.acmicpc.net/problem/10845
import sys


def input():
    return sys.stdin.readline()


n = int(input())
queue = []
for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        queue.append(command[1])
    if command[0] == 'pop':
        if len(queue) > 0:
            print(queue[0])
            queue = queue[1:]
        else:
            print(-1)
    if command[0] == 'size':
        print(len(queue))
    if command[0] == 'empty':
        if len(queue) > 0:
            print(0)
        else:
            print(1)
    if command[0] == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    if command[0] == 'back':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
