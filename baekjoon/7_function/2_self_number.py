# 셀프 넘버
# 1
result = [i for i in range(10001)]


for num in range(1,10001):
    # temp에 self num를 계산해서 넣어줌
    temp = num + sum([int(n) for n in str(num)])
    # print(temp)
    # temp가 10000이 넘으면 저장하지 않음
    if temp > 10000: 
        continue
    # self number를 인덱스로 가지는 원소를 0으로
    result[temp] = 0

# result 배열을 돌면서 원소가 0이 아니면 출력
for num in result:
    if num != 0: print(num)



# 2
result = [0] + [1] * 10000


for num in range(1,10001):
    # temp에 self num를 계산해서 넣어줌
    temp = num + sum([int(n) for n in str(num)])
    # print(temp)
    # temp가 10000이 넘으면 저장하지 않음
    if temp > 10000: 
        continue
    # self number를 인덱스로 가지는 원소를 0으로
    result[temp] = 0

# result 배열을 돌면서 원소가 0이 아니면 인덱스를 출력
for ind, value in enumerate(result):
    if value != 0: print(ind)