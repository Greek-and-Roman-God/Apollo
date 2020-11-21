# 셀프 넘버

result = [i for i in range(10001)]

for num in range(10001):
    if num != 0:

        temp = num + sum([int(n) for n in str(num)])
        # print(temp)
        if temp > 10000: 
            continue
        result[temp] = 0
for num in result:
    if num != 0: print(num)