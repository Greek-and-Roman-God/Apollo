# 10799 쇠막대기
# https://www.acmicpc.net/problem/10799

stick_laser = input()

stack = []
answer = 0
for i, stick in enumerate(stick_laser):
    if stick == '(':
        stack.append(stick)
    else:
        stack.pop()
        if stick_laser[i-1] == '(':
            answer += len(stack)
        else:
            answer += 1
print(answer)
