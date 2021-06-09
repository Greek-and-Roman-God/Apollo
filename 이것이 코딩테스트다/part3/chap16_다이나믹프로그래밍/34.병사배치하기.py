# 병사배치하기
# https://www.acmicpc.net/problem/18353
n = int(input())
pawn = list(map(int, input().split()))
# 감소하는 수열의 최대 길이를 저장할 dp
dp = [1] * n

# i까지의 수열에서 감소하는 수열의 길이가 최대 얼마인지 확인
for i in range(1, n):
    # 0 ~ i까지 돌면서 i와 j의 전투력을 비교하고 j의 전투력이 더 높다면(순서가 올바르다면)
    for j in range(i):
        if pawn[i] < pawn[j]:
            # 앞 병사의 전투력이 더 강하다면 올바른 순서이니까
            # j 병사까지의 최대길이인 dp[j]에 i 병사 한명을 추가한 dp[j] + 1 과
            # 안쪽 for문을 돌면서 저장되어있는 dp[i] 중
            # 최댓값을 dp[i]에 저장해줌
            dp[i] = max(dp[i], dp[j] + 1)
# print(dp)
# dp가 가지고 있는 최대 값이 감소하는 수열의 최대 길이
# 원래 병사의 수인 n에서 dp의 최댓값을 빼서 열외된 병사의 수를 구함
print(n - max(dp))

# 2
# n = int(input())
# pawn = list(map(int, input().split()))
# pawn.reverse()

# dp = [1] * n

# for i in range(1, n):
#     for j in range(i):
#         if pawn[i] > pawn[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(n - max(dp))
