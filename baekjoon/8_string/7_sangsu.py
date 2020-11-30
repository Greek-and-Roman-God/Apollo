# 2908 상수
# https://www.acmicpc.net/problem/2908

# 입력을 공백을 기준으로 나눠서 numbers list에 넣어줌
num1, num2 = input().split()

# 뒤집은 문자열을 정수형으로 변환하여 변수에 다시 대입해줌
num1 = int(num1[::-1])
num2 = int(num2[::-1])

# 큰수를 출력
print(num1 if num1 > num2 else num2)
