# Q2 곱하기 혹은 더하기
list = list(input())
result = 0
for item in list:
    if int(item) * result > int(item) + result:
        result = result*int(item)
    else:
        result = result + int(item)
print(result)