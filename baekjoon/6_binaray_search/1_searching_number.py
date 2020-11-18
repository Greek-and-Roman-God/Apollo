# 수찾기
n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))

temp = m_list[:]
answer = []

for num in temp:
    start = 0
    end = n - 1
    while 1:
        center = (start + end)//2
        if n_list[center] == num:
            # answer.append(1)
            print(1)
            break
        elif n_list[center] < num:
            start = center + 1
        else:
            end = center - 1
        if start > end:
            # answer.append(0)
            print(0)
            break

# print(answer)
# for num in m_list:
#     for res, res_num in answer:
#         if num == res_num:
#             print(res)
#             break

# sorted(answer, key=lambda x: m_list)
# print(answer)
