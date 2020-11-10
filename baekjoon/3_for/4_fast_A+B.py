import sys

cnt = int(input())
for i in range(cnt):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)