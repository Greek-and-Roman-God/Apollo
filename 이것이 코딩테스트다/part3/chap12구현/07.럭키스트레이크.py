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


# 2021-08-13
score = list(map(int, list(input()))

score1 = score[:len(score) // 2]
score2 = score[len(score) // 2:]

if sum(score1) == sum(score2):
    print("LUCKY")
else:
    print("READY")

