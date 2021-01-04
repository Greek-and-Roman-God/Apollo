# 14888 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
from itertools import permutations

n = int(input())
a = input().split()
oper = input().split()

operator = ['+', '-', '*', '/']
oper_str = ''
for o, num in zip(operator, oper):
    oper_str += o * int(num)
oper_str = list(set(list(map(''.join, permutations(oper_str)))))

results = []


for oper in oper_str:
    # print(oper, end=' ')
    result = a[0]
    i = 1
    for o in oper:
        if o == '/':
            o = '//'
        # print(str(result) + o + a[i], end=' ')
        if int(result) < 0 and o == '//':
            result = - eval(str(-result) + o + a[i])
        else:
            result = eval(str(result) + o + a[i])
        i += 1
    # print(result)
    results.append(result)


print(max(results))
print(min(results))
