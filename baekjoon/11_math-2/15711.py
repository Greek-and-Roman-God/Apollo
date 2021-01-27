# 15711 환상의 짝꿍
# https://www.acmicpc.net/problem/15711
t = int(input())

# 주어진 범위의 **(1/2)만큼만 확인하면 나머지 수들의 소수 판단은
# 구해진 소수들로 나눠보면 됨
num = 2*(10**6)
prime = [0] * (num+1)
prime[0] = 1
prime[1] = 1
for i in range(2, num//2+1):
    if prime[i] == 0:
        for j in range(i+i, num+1, i):
            prime[j] = 1

prime_num = []  # 소수만 들어 있는 배열
for i in range(3, num+1):
    if prime[i] == 0:
        prime_num.append(i)


def is_prime(num):
    global prime_num

    for prime in prime_num:
        if num//2 < prime:
            break
        if num % prime == 0:
            return False
    return True


for _ in range(t):
    a, b = map(int, input().split())
    hap = a+b

    if hap <= 3:
        print('NO')
    elif hap % 2 == 0:
        print('YES')
    elif is_prime(hap-2):
        print('YES')
    else:
        print('NO')
