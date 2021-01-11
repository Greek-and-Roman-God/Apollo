# 9663 N-Queen
# https://www.acmicpc.net/problem/9663
n = int(input())
board = [0] * n
d1 = [0] * (2*n-1)
d2 = [0] * (2*n-1)
answer = 0


def sol(i):
    global answer
    if i >= n:
        answer += 1
    for j in range(n):

        if board[j] or d1[i+j] or d2[n-1+j-i]:
            continue

        board[j] = d1[i+j] = d2[n-1+j-i] = 1
        sol(i+1)
        board[j] = d1[i+j] = d2[n-1+j-i] = 0


sol(0)
print(answer)

# board[i][j]
# 공격할 수 있는 경우
# - i가 같은 경우, j가 같은 경우
# - 대각선 ->
