# 성적이 낮은 순서로 학생 출력하기
n = int(input())
datas = []
for _ in range(n):
    datas.append(input().split())
    datas[-1][-1] = int(datas[-1][-1])
datas.sort(key=lambda x: x[1])

for data in datas:
    print(data[0], end=" ")
