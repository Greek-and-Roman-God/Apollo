# 평균
cnt = int(input())
scores = list(map(int,input().split()))
max_scor = max(scores)

scores = [score/max_scor*100 for score in scores]
aver = sum(scores)/len(scores)
print(aver)