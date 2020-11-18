# 랜선 자르기
def cutting_wire():
    n, k = map(int, input().split())
    wires = []
    for _ in range(n):
        wires.append(int(input()))

    temp = max(wires)

    limit = 0
    m_value = 0
    m_cnt = 0
    while 1:
        cnt = 0
        for wire in wires:
            cnt += wire // temp
            print(f'cnt {cnt} temp {temp} m_cnt {m_cnt}')
        print('------------------')
        if cnt == m_cnt and temp == m_value:
            print(temp)
            break

        if cnt >= k:
            m_cnt = cnt
            m_value = temp
            temp = temp + temp//2
        elif cnt < m_cnt:
            temp = (m_value+temp)//2
        else:
            temp = temp//2

        # limit+=1
        # if limit > 100:
        #     break

cutting_wire()