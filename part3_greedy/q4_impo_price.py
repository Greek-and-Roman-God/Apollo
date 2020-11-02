# Q4 만들 수 없는 금액
count = input()
coin_list = list(map(int,input().split(' ')))
test_list = [item for item in range(1, 1000001)]
for num in test_list:
    temp = num
    for coin in coin_list:
        if temp - int(coin) >= 0: 
            temp = temp - int(coin)
        if temp == 0: break
    if temp != 0:
        result = num
        break
print(result)