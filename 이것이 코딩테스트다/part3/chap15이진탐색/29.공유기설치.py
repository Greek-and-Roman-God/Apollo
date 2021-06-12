# 공유기 설치
#
import sys
n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))
# 집을 c개 고르는 모든 경우
# 그 중 가장 가까운 공유기의 거리가 최대인 경우 그 거리를 구하기
# 정렬된 houses에서 c개를 뽑아서 제일 가까운 공유기의 거리가 얼마인지 확인..
# 뭘 기준으로 이분탐색을 해야하지?
# 1 2 4 8 9
#  1 2 4 1

# 풀이
# https://claude-u.tistory.com/448
n, c = map(int, input().split())
house = [int(sys.stdin.readline()) for _ in range(n)]

# 해당 거리를 유지하며 공유기가 몇 개 설치될 수 있는가?


def router_counter(distance):
    count = 1
    cur_house = house[0]  # 시작점
    for i in range(1, N):  # 집모두를 돈다
        if cur_house + distance <= house[i]:  # 이전 집에서 해당 거리보다 멀리 떨어진 집이라면
            count += 1
            cur_house = house[i]  # 공유기 설치된 집 갱신
    return count


house = sorted(house)  # 이분탐색을 위한 정렬
start, end = 1, house[-1] - house[0]  # 1, 첫집과 끝집

while start <= end:  # 이분탐색 알고리즘
    mid = (start+end) // 2

    if router_counter(mid) >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
