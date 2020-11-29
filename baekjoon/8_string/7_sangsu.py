# 2908 상수
# https://www.acmicpc.net/problem/2908

# 입력을 공백을 기준으로 나눠서 numbers list에 넣어줌
num1, num2 = input().split()
num1 = int(num1[::-1])
num2 = int(num2[::-1])
print(num1 if num1 > num2 else num2)
