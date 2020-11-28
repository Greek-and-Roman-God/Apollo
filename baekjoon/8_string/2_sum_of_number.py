# 11720 숫자의 합
# https://www.acmicpc.net/problem/11720

length = int(input('개수: '))
num_str = input('계산할 숫자문자열: ')

result = 0
for num in num_str:
    result += int(num)

print(result)