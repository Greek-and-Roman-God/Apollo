# 14889 스타트와 링크
# https://www.acmicpc.net/problem/14889
n = int(input())
ss = []
for _ in range(n):
    s = list(map(int, input().split()))
    ss.append(s)

visited = [0] * n
answer = 1000000000


def dfs(idx, cnt):
    global answer
    if cnt == n//2:
        start, link = 0, 0

        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += ss[i][j]
                elif not visited[i] and not visited[j]:
                    link += ss[i][j]
        answer = min(answer, abs(start - link))

    for i in range(idx, n):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(i+1, cnt+1)
        visited[i] = 0


dfs(0, 0)
print(answer)
