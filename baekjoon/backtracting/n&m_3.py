# 15651 N과 M (3)
# https://www.acmicpc.net/problem/15651
n, m = map(int, input().split())
answer = [None] * m


def dfs(i):
    if i == m:
        for a in answer:
            print(a, end=' ')
        print()
        return
    for j in range(1, n+1):
        answer[i] = j
        dfs(i+1)


dfs(0)
