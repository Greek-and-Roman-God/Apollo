# 랜선 자르기
def cutting_wire():
    n, k = map(int, input().split())
    wires = []
    for _ in range(n):
        wires.append(int(input()))

    temp = min(wires)

    while 1:
        limit = 0
        cnt = 0
        for wire in wires:
            cnt += wire // temp
            print(f'cnt {cnt} temp {temp}')
        print('------------------')
        if cnt >= k:
            temp = temp + 9
            break
        temp = temp - 10

 
    for i in range(temp, temp-10,-1):
        cnt = 0
        
        for wire in wires:
            cnt += wire // i
            print(f'out cnt {cnt} temp {i}')
        print('------------------')

        if cnt >= k:
            print(i)
            break
cutting_wire()