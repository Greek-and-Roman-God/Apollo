# 14888 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
# from itertools import permutations

# n = int(input())
# a = input().split()
# oper = input().split()

# operator = ['+', '-', '*', '/']
# oper_str = ''
# for o, num in zip(operator, oper):
#     oper_str += o * int(num)
# oper_str = list(set(list(map(''.join, permutations(oper_str)))))

# results = []


# for oper in oper_str:
#     # print(oper, end=' ')
#     result = a[0]
#     i = 1
#     for o in oper:
#         if o == '/':
#             o = '//'
#         # print(str(result) + o + a[i], end=' ')
#         if int(result) < 0 and o == '//':
#             result = - eval(str(-result) + o + a[i])
#         else:
#             result = eval(str(result) + o + a[i])
#         i += 1
#     # print(result)
#     results.append(result)


# print(max(results))
# print(min(results))


# permutations 안 쓰고 풀기
n = int(input())
a = list(map(int, input().split()))
oper = list(map(int, input().split()))

max_result = -10000000001
min_result = 10000000001


def dfs(plus, minus, multi, divide, cnt, sum):
    global max_result, min_result
    if cnt == n:
        max_result = max(max_result, sum)
        min_result = min(min_result, sum)
        print(max_result, min_result)

    if plus > 0:
        dfs(plus-1, minus, multi, divide, cnt + 1, sum + a[cnt])
    if minus > 0:
        dfs(plus, minus-1, multi, divide, cnt + 1, sum - a[cnt])
    if multi > 0:
        dfs(plus, minus, multi-1, divide, cnt + 1, sum * a[cnt])
    if divide > 0:
        dfs(plus, minus, multi, divide-1, cnt + 1, sum / a[cnt])


dfs(oper[0], oper[1], oper[2], oper[3], 1, a[0])
print(max_result)
print(min_result)
