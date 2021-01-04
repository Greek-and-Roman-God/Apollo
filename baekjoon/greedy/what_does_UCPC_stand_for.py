# 15904 UCPC는 무엇의 약자일까?
# https://www.acmicpc.net/problem/15904

string = input()

ucpc = "UCPC"
i = 0
for s in string:
    if s.isupper:
        if s == ucpc[i]:
            i += 1
    if i == 4:
        break
if i == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')
