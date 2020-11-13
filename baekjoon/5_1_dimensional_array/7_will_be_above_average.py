# 평균은 넘겠지
case_cnt = int(input())
classes = []
for _ in range(case_cnt):
    classes.append(list(map(int,input().split())))

for data in classes:
    aver = sum(data[1:])/data[0]

    std_cnt = 0
    for score in data[1:]:
        if score > aver: std_cnt += 1
    
    std_aver = std_cnt/data[0]*100
    print("%.3f"%std_aver+"%")