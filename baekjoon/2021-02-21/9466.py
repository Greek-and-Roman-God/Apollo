# 텀 프로젝트
# https://www.acmicpc.net/problem/9466
t = int(input())


for _ in range(t):
    n = int(input())
    choice = list(map(int, input().split()))
    check = [0] * n
    cnt = n

    def dfs(i):
        if i == n:
            return
