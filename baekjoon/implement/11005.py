# 1005 진법 변환 2
# https://www.acmicpc.net/problem/11005
n, b = map(int, input().split())
result = ''

codes = {}
for i, code in zip(range(10, 36), range(65, 91)):
    codes[str(i)] = chr(code)

while n > 0:
    temp = n % b
    n = n // b
    if temp > 9:
        result += codes[str(temp)]
    else:
        result += str(temp)
print(''.join(list(reversed(result))))
