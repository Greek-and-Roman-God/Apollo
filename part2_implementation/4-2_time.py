# 시각
h_limit = int(input())
answer = 0

h_case = [1, h_limit]
if h_limit > 22: h_case = [3, h_limit-2]
elif h_limit > 12: h_case = [2, h_limit-1]
elif h_limit > 2: h_case = [1, h_limit]
m_case = [15,45]
s_case = [15,45]
for h in h_case:
    for m in m_case:
        for s in s_case:
            print(f'{h}*{m}*{s}')
            answer += h*m*s
answer = answer - h_case[-1]*m_case[-1]*s_case[-1]

print(answer)