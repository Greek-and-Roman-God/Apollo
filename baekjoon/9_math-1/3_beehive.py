# 2292 벌집

N = int(input())

num = 1
dist = 1
while num < N:
    num += 6 * dist
    dist += 1

print(dist)

'''
for num in [1, 2, 3, 4, 5, 6]:
    plus = 1
    cnt = 0
    while up-1 > cnt:
        plus += num + 6 * cnt
        cnt += 1
    print(f'plus {plus}')

    if plus == N:
        break
    elif plus > N:
        up += plus - N
        break
# print(temp, up)
'''
