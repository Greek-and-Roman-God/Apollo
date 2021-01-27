# 1644 소수의 연속합
# https://www.acmicpc.net/problem/1644

num = int(input())

# 체를 만들어서 소수를 구함
prime = [0] * (num+1)
prime[0] = 1
prime[1] = 1
for i in range(2, num//2+1):
    if prime[i] == 0:
        for j in range(i+i, num+1, i):
            prime[j] = 1

prime_num = []  # 소수만 들어 있는 배열
for i in range(num+1):
    if prime[i] == 0:
        prime_num.append(i)

# 반복문을 돌면서 연속하는 값들의 합이 조건을 만족하는지 확인
answer = 0
i = 0   # 연속 수열에서 시작값
while i < len(prime_num):
    temp = 0
    for j in range(i, len(prime_num)):
        temp += prime_num[j]
        if temp > num:  # 연속수열의 합이 커지면 시작값만 바꿔주고 break
            i += 1
            break
        elif temp == num:   # 연속수열의 합이 조건과 같으면 정답+1하고 다른 경우의 수를 확인하기 위해 시작값을 바꿔주고 break
            answer += 1
            i += 1
            break
    else:
        i += 1  #


print(answer)
