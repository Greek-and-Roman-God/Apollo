# 9613 GCD 합
# https://www.acmicpc.net/problem/9613

def gcd(a, b):
    result = 0
    if a > b:
        a, b = b, a
    while b > 0:
        result = b
        a, b = b, a % b
    return result


t = int(input())

for _ in range(t):
    inp = list(map(int, input().split()))
    cnt = inp[0]
    num_list = inp[1:]

    answer = 0
    while num_list:
        num = num_list.pop(0)
        temp = 0
        for n in num_list:
            temp += gcd(num, n)

        answer += temp
    print(answer)
