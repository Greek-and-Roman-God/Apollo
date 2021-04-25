# 모험가 길드
n = int(input())
people = list(map(int, input().split()))
people.sort()
print(people)
i = people[0]
answer = 0
while i < len(people):
    temp = 0
    for _ in range(i):
        p = people.pop(0)
        temp = max(temp, p)
    if temp <= i:
        i = people[0]
        answer += 1
    else:
        break
print(answer)

# 답지
answer = 0
cnt = 0
for i in people:
    cnt += 1
    if i <= cnt:
        cnt = 0
        answer += 1
print(answer)
