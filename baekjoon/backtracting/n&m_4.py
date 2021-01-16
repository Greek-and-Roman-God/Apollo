# n&m 4
# https://www.acmicpc.net/problem/15652
n, m = map(int, input().split())
nums = [0 for _ in range(n)]
answer = []


def dfs(i):
    if i == m:
        print(*answer)
        return
    for j in range(n):
        if nums[j] == 0:
            answer.append(j+1)
            dfs(i+1)
            nums[j] = 1

            answer.pop()

            for k in range(j+1, n):
                nums[k] = 0


dfs(0)
