# 6588 골드바흐의 추측
# https://www.acmicpc.net/problem/6588

# 통과
# 체를 만들어서 소수를 구함
num = 10000000
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

# print(prime_num)
while 1:
    n = int(input())
    if n == 0:
        break

    # 만들 수 있는 조합 찾기
    for i in range(len(prime_num)):
        temp = prime_num[i]

        if prime[n-temp] == 0:
            print(n, '=', temp, '+', n-temp)
            break

# 시간초과
# 체를 만들어서 소수를 구함
num = 10000000
prime = [0] * (num+1)
prime[0] = 1
prime[1] = 1
for i in range(2, num//2+1):
    if prime[i] == 0:
        for j in range(i+i, num+1, i):
            prime[j] = 1

# prime_num = []  # 소수만 들어 있는 배열
# for i in range(3, num+1):
#     if prime[i] == 0:
#         prime_num.append(i)

# print(prime_num)
while 1:
    n = int(input())
    if n == 0:
        break

    # 만들 수 있는 조합 찾기
    for i in range(n):
        # print(i, prime[i], prime[n-i])
        if prime[i] == 0 and prime[n-i] == 0:
            print(n, '=', i, '+', n-i)
            break
