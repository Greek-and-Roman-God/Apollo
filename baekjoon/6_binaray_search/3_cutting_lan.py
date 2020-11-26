# 랜선 자르기
def cutting_wire():
    n, k = map(int, input().split())
    wires = []
    for _ in range(n):
        wires.append(int(input()))

    temp = max(wires) # 잘라질 길이
    m_temp = 0 # 중간 길이
    m_cnt = 0 # 중간 개수
    while 1:
        cnt = 0
        for wire in wires: # temp로 잘랐을 때 나오는 조각들의 수를 반복문을 돌면서 계산
            cnt += wire // temp
        #     print(f'cnt {cnt} temp {temp} m_cnt {m_cnt} m_temp {m_temp}')
        # print('------------------')

        if cnt == m_cnt and temp == m_temp: # 무한 루프를 막기 위한 탈출 조건
            print(temp)
            break
        
        
        if cnt >= k: # 필요한 개수보다 구해진 개수가 크거나 같으면 = temp가 짧다는 것
            # cnt == k 인 경우 이 때의 temp가 답일 수 있지만
            # 더 길고 cnt도 맞출 수 있는 temp가 있을 수도 있기 때문에
            # 조건문을 통과한 temp보다 더 긴 길이를 탐색해보기 위해서 일단 변수로 저장
            m_cnt = cnt
            m_temp = temp

            temp = temp + temp//2 # 잘라질 크기 늘이기
        
        elif cnt < m_cnt: # 저장된 직전 개수보다 작아지면
            temp = (m_temp + temp) // 2 # 저장된 길이 와 temp 사이의 값을 temp에 대입
            # m_cnt와 m_temp가 저장된 이후에는
            # m_temp와 temp 사이에서 값을 찾아야하기 때문에 두번째 조건문까지만 돌게됨

        elif cnt < k: # 필요한 개수보다 구해진 개수가 작을 경우 = temp가 길다는 것
            temp = temp // 2 # 필요한 개수보다 작은 경우 반절로 자르기

"""
1. 가장 긴 랜선의 길이를 temp로 잡고 이등분을 하면서 탐색을 한다.
2. 탐색을 하다보면 구해야하는 값을 넘어가거나 값과 같아지는 지점이 생김
   - 이 때 길이의 1.5배를 하고 값이 넘어간 길이와 개수를 저장
   - temp가 답일 수도 있지만 더 긴 temp가 있을 수도 있기 때문에 이 때의 길이와 개수를 변수로 저장함
3. 2에서 저장한 지점과 1.5배한 temp 사이의 중간 값을 탐색
4. 또 구해야하는 값을 넘어가거나 값과 같아지는 지점이 생김 
   - 똑같이 길이를 1.5배하고 값이 넘어간 길이와 개수를 저장

5. 이걸 계속 반복하면 저장된 temp에는 cnt를 넘기는 temp -> cnt는 맞지만 길이가 최대인지 확실하지 않은  temp가 남게 된다.

   - temp가 최대 길이인지 판단하기

     처음 첫번째 조건문(`cnt >= k`)에 `True`가 나왔을 때의 temp를 편의상 T라고 하겠다. 
     이 이후로 temp에는 1.5*temp가 담기게 되고 그 후로는 T와 temp 사이의 값을 탐색하게 되므로 이 이후에 계산된 temp는 T를 넘을 수 없다. 
     때문에 첫번째 조건문(`cnt >= k`)을 통과하는 temp는 T보다 무조건 길다. 그렇게 점점 긴 temp가 첫번째 조건문(`cnt >= k`)을 통과하다보면 
     결국에는 `cnt == k`이고 가장 긴 temp가 m_temp에 들어가게 된다. 그리고 가장 긴 m_temp가 구해진 이후로는 더 이상 첫번째 조건을 통과하는 
     경우가 m_temp와 temp 사이에 없기 때문에 m_temp가 바뀌지 않아 똑같은 루트를 반복하게 된다. 
     cnt와 temp가 각각 m_cnt, m_temp와 같을 경우 똑같은 루프가 돌고 있다 = 결과를 구했다. 라고 판단하고 탈출하게 했다.
"""
cutting_wire()