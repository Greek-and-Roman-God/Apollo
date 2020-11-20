# 숫자 카드 2

# 1
# 찾을 번호리스트를 반복문에 넣고 돌려서 count 함수로 개수 출력하기
'''
n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

temp = m_list[:]

for num in temp:
    print(f'{n_list.count(num)}', end=' ')
'''
# 2
# n = int(input())
n = 10
# n_list = list(map(int,input().split()))
n_list = [6,3,2,10,10,10,-10,-10,7,3]
# m = int(input())
m = 8
# m_list = list(map(int,input().split()))
m_list = [10,9,-5,2,3,4,5,-10]
n_list.sort()
print(f'정렬된 n_list {n_list}')
temp = m_list[:]
answer = []
for num in m_list:
    temp = -1
    start = 0
    end = len(n_list) - 1
    limit = 0
    while 1:
        flag = True
        limit += 1
        count = 0
        temp = (end+start)//2
        #print(f'num {num} n_list[temp] {n_list[temp]} temp {temp} start {start} end {end}')
        if end - start == 1:
            print(count,end=' ')

            #print(f'----------------- count {count}')
            # answer.append(count)
            break
        if n_list[temp] < num:
            flag = False
            start = temp
        elif n_list[temp] > num:
            flag = False
            end = temp
        else:
            while 1:
                limit += 1
                flag = True
                #print(f'else: num {num} n_list[temp] {n_list[temp]}')

                if n_list[start+1] != num and n_list[start] != num:
                    start = (temp + start)//2
                    flag = False
                    # print(f'start: start {start} end {end} temp {temp}')
                if n_list[end] != num:
                    end = temp + (end - temp)//2
                    flag = False
                    # print(f'end: start {start} end {end} temp {temp}')


                if flag:
                    count += end - start
                    # print(f'------------------ count {count}')
                    # answer.append(count)
                    print(count,end=' ')
                    break
        if flag:
            break
# print(answer)

