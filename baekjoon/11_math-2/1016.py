# 1016 제곱 ㄴㄴ 수
# https://www.acmicpc.net/problem/1016

# 다시 풀어보기
import sys
import math

# results = []
# min_num, max_num = map(int, sys.stdin.readline().split())
# validation = [1 for _ in range(min_num, max_num+1)]

# search_target = int(math.sqrt(max_num))
# # max의 값보다 작은 모든 제곱수의 목록을 생성
# squares = [v**2 for v in range(2, search_target+1)]
# for square in squares:
#     # min부터 max까지의 수 중, 해당 제곱수의 최소의 배수를 구함.
#     cur_idx = (math.ceil(min_num / square) * square) - min_num
#     while cur_idx <= max_num - min_num:
#         # 제곱수의 배수인 경우 0으로 대체
#         validation[cur_idx] = 0
#         # 다음 제곱수의 index를 구함.
#         cur_idx += square

# # 남은 1들의 개수가 제곱 ㄴㄴ수의 개수가 된다.
# result = sum(validation)
# results.append(result)

# for result in results:
#     sys.stdout.write(str(result))


# 겹치는 값 때문에 안됨
# min, max = map(int, input().split())

# end_num = int(math.sqrt(max))
# squares = [i**2 for i in range(2, end_num+1)]

# cnt = 0
# for square in squares:
#     cnt += max // square - min // square
# print(max-min+1-cnt)

min, max = map(int, input().split())

end_num = int(math.sqrt(max))
squares = [i**2 for i in range(2, end_num+1)]
valid = [0] * (max-min+1)
for square in squares:
    temp = math.ceil(min/square) * square
    while temp <= max:
        valid[temp-min] = 1
        temp += square
print(valid.count(0))
