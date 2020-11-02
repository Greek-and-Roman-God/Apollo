# Q6 무지의 먹방 라이브
# 푸는 중
def solution(food_times, k):

    times = 0
    for food in food_times: times += food
    if times <= k: return -1

    while 1:
        for time in range(0,len(food_times)):
            if not k: return time+1
            if food_times[time]:
                food_times[time] -= 1
                k-=1

print(solution([3,1,2],5))