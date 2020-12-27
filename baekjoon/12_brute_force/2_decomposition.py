# 분해합
# https://www.acmicpc.net/problem/2231
n = int(input())

for number in range(1, n):
    temp = [number]
    for num in str(number):
        temp.append(int(num))

    if sum(temp) == n:
        print(number)
        break
else:
    print(0)


# 다른 사람 풀이
n = input()
num = int(n)
start = max(num - 9*len(n), 0)
res = []
for i in range(start, num):
    if num == sum(map(int, str(i)))+i:
        res.append(i)
if len(res) == 0:
    print(0)
else:
    print(min(res))
