# 1406 에디터
# https://www.acmicpc.net/problem/1406
import sys


def input():
    return sys.stdin.readline().strip()


left = list(input())
right = []
m = int(input())
for _ in range(m):
    command = input().split()

    if command[0] == 'L':
        if len(left) != 0:
            right.append(left.pop())
    elif command[0] == 'D':
        if len(right) != 0:
            left.append(right.pop())
    elif command[0] == 'B':
        if len(left) != 0:
            left.pop()
    elif command[0] == 'P':
        left.append(command[1])
print(''.join(left + list(reversed(right))))
# sort()를 쓰고 더하는 것보다 reversed()가 더 빠름

# 1
# string=input()
# cursor=len(string)
# m=int(input())
# for _ in range(m):
#     command=input().split()

#     if command[0] == 'L':
#         if cursor != 0:
#             cursor -= 1
#     if command[0] == 'D':
#         if cursor != len(string) + 1:
#             cursor += 1
#     if command[0] == 'B':
#         if cursor != 0:
#             string=string[:cursor] + string[cursor+1:]
#             cursor -= 1
#     if command[0] == 'P':
#         string=string[:cursor] + command[1] + string[cursor:]
#         cursor += 1

# print(string)
