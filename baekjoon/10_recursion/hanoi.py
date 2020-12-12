# 11729 하노이 탑 이동 순서
# https://www.acmicpc.net/problem/11729

N = int(input())


def hanoi(no, x, y):
    move = []
    if no > 1:
        move += hanoi(no - 1, x, 6 - x - y)
    move += [[x, y]]
    if no > 1:
        move += hanoi(no - 1, 6 - x - y, y)

    return move


answer = hanoi(N, 1, 3)
print(len(answer))
# print(answer)
for m in answer:
    print(m[0], m[1])
