# 11720 숫자의 합
# https://www.acmicpc.net/problem/11720

# 백준에서 input안에 문자열을 집어넣을 경우 런타임에러
length = int(input('개수: '))
num_str = input('계산할 숫자문자열: ')

# - 입력받은 문자열의 길이만큼 반복문을 돌려서 결과를 계산
#   1. python에서 문자열을 하나씩 잘라내어 연산이 가능하므로 문자열형태로 떼어내어 정수형으로 변환해준 후 결과값을 계산
result = 0
for num in num_str:
    result += int(num)

print(result)