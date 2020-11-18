# 숫자 카드 2
n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

temp = m_list[:]

for num in temp:
    print(f'{n_list.count(num)}', end=' ')
