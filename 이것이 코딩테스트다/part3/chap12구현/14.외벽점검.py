# 외벽점검
# https://programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1

    length = len(weak)

    for i in range(length):
        weak.append(n+weak[i])

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count-1]

            for i in range(start, start + length):
                # print(count, weak[i], position)
                if position < weak[i]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[i] + friends[count-1]
            # print("=================================")
            answer = min(answer, count)
    if answer > len(dist):
        return -1

    return answer

# 원형으로 구성된 데이터가 주어지면 길이를 2배 늘여서 일자 형태로 만들어주면 문제를 푸는데 용이하다.
#   2배로 늘인 후 다룰 길이 만큼을 잘라서 연산하면 반대로 돌아가는 경우를 따로 생각하지 않아도 됨
