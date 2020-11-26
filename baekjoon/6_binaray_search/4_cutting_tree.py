# 나무 자르기
#1
# from math import ceil

# n, need = map(int,input().split())
# tree_h = list(map(int,input().split()))

# tree_h.sort()
# tree_h.reverse()

# i = 0
# count = 1
# log = 0
# while 1:
#     log += (tree_h[i] - tree_h[i+1]) * count
#     if log >= need:
#         # tree_h[i] > answer > tree_h[i+1]
#         answer = tree_h[i] - ceil((log - need)/count) if log != need else tree_h[i+1]
#         break
#     i += 1
#     count += 1

# print(answer)

#2

# n, need = map(int,input().split())
# tree_h = list(map(int,input().split()))

# # 큰 나무부터 내림차순으로 정렬
# tree_h.sort()

# i = 0
# count = 1
# log = 0
# while 1:

#     # 나무들의 길이 기준으로 나무를 잘랐을 때의 길이를 계산
#     log += (tree_h[i-1] - tree_h[i-2]) * count
#     # 자른 나무의 길이가 필요 이상일 경우
#     if log >= need:
#         log -= (tree_h[i-1] - tree_h[i-2]) * count
        
#         start = tree_h[i-2] # 작은 나무
#         end = tree_h[i-1] # 큰 나무

#         while True:

#             mid = (end + start) // 2 # 중간
#             temp = log + (tree_h[i-1] - mid) * count
#             # print(f'start {start} mid {mid} end {end} temp {temp}')


#             if  temp > need and start != mid:
#                 start = mid
#             elif temp < need:
#                 end = mid
#             # if temp == need:
#             else:
#                 answer = mid
#                 break
#         break
#     i -= 1
#     count += 1

# print(answer)

#3
n, need = map(int,input().split())
tree_h = list(map(int,input().split()))

start = max(tree_h)
end = 0

answer = 0
while start >= end:

    mid = (start + end) // 2
    temp = 0

    for log in tree_h:
        temp += log - mid if log - mid > 0 else 0
    
    if temp >= need: # 길이가 넘침
        end = mid + 1
        answer = mid
    elif temp < need: # 길이가 모자람
        start = mid - 1

print(answer)