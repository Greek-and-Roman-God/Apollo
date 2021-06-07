# 퇴사
#
# 상담을 완료하는데 걸리는 시간 t
# 받을 수 있는 금액 p

# 1 마지막 예시가 안 풀림 -> 예약을 이어서 하지 않을 수도 있음
# n = int(input())
# reserv = []
# for _ in range(n):
#     reserv.append(list(map(int, input().split())))
# income = 0
# for i in range(n):
#     t = i
#     p = 0
#     # 끝나는 날을 맞출 수 있는지 확인 -> 수입 더하기
#     while t + reserv[t][0] < n:
#         print(f'현재 날짜 {t} 다음 날짜 {t + reserv[t][0]}')
#         p += reserv[t][1]
#         t += reserv[t][0]
#         print(f'현재까지 수입 {p}')
#     if t + reserv[t][0] < n:
#         p += reserv[t][1]
#     income = max(p, income)
#     print(f'최고 수익 {income}=============================')

# 2
n = int(input())
reserv = []
for _ in range(n):
    # 소요시간, 수익, 이전에 낸 수익의 최댓값을 담을 원소 하나 추가
    reserv.append(list(map(int, input().split())) + [0])
# 일별 최대 수익을 저장할 dp 리스트
dp = [0] * (n)

for i in range(n):
    # 이전에 낸 수익의 최댓값을 현재 dp에 넣어줌
    dp[i] = reserv[i][2]
    # 현재 일의 소요시간이 퇴사날을 지나지 않는지 확인하기 위해 (현재 시간 + 소요시간) -> 다음 일을 시작할 수 있는 날
    t = i + reserv[i][0]
    # 일이 끝나는 날을 퇴사날에 맞출 수 있는지 확인 (t는 다음 일을 시작할 수 있는 날짜라서 퇴사 전날에 맞춰서 일이 끝날 경우 t는 n이 나온다. 그래서 n을 포함한 조건문을 써줌)
    if t <= n:
        # 일이 끝난 날이 퇴사 전이면 i일의 일을 할 수 있는 것이므로 dp에 i일의 수익을 더해줌
        dp[i] += reserv[i][1]
        # t부터 n까지에 dp[i]의 수익을 저장해준다.
        for j in range(t, n):
            reserv[j][2] = max(reserv[j][2], dp[i])
print(reserv)
print(dp)
print(max(dp))
