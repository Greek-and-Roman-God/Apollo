# 2810 컵홀더
# https://www.acmicpc.net/problem/2810

# 컵홀더의 개수?
# 일반좌석의 개수와 커플석의 개수
# 일반좌석만 있을 경우 컵홀더의 개수는 좌석 + 1
# 커플석은 사이에 컵홀더가 없으므로 커플석이 있으면 컵폴더의 개수는 (좌석+1)-커플석의수 -> 이게 정답

n = int(input())
sheets = input()
cuple_cnt = sheets.count('LL')
holder = n+1-cuple_cnt
# 컵홀더의 수가 사람 수 보다 많은 경우를 생각하지 못함....
if holder > n:
    print(n)
else:
    print(holder)
