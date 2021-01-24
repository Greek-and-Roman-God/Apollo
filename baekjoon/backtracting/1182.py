# 1182 부분수열의 합
# https://www.acmicpc.net/problem/1182
n, s = map(int, input().split())
num_lst = list(map(int, input().split()))
answer = 0


def dfs(sum, i):
    global answer
    if i == n:
        return
    if sum+num_lst[i] == s:
        answer += 1

    dfs(sum, i+1)
    dfs(sum+num_lst[i], i+1)


dfs(0, 0)
print(answer)
# 값이 포함되거나 포함되지 않거나의 경우만 존재하므로 두 경우로 재귀를 돌리면 모든 경우의 수를 확인할 수 있다.
# 왜 현재까지의 sum에 가리키고 있는 수를 더한 값을 확인하는거지?
