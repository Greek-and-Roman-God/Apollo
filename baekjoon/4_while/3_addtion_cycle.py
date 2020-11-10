    # 더하기 사이클
num = input()
test = num[:]
cnt = 0
while 1:
    if len(test) == 1: test = "0"+test
    temp = int(test[0])+int(test[1])
    test = test[1]+str(temp)[-1:]
    #print(test)
    cnt += 1
    if int(test) == int(num): break
print(cnt)