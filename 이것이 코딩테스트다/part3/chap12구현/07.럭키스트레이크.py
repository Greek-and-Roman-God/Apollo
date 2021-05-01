# 럭키 스트레이크
def cal(score):
    score = list(map(int, list(score)))
    return sum(score)


n = input()

score1 = n[:len(n)//2]
score2 = n[len(n)//2:]

if cal(score1) == cal(score2):
    print("LUCKY")
else:
    print("READY")
