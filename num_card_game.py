def num_card_game():
  N,M = map(int, input().split())

  result = 0

  while 1:
    row = list(map(int, input().split()))
    row.sort() # 입력받은 행을 정렬

    if row[0] > result: result = row[0] # 가장 작은 수를 result에 저장
    N -= 1

    if N == 0: break

  print(result)

def game_ex1():
  # N,M을 공백을 구분하여 입력받기
  N,M = map(int, input().split())

  result = 0

  for i in range(N):
    data = list(map(int,input().split()))

    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # 가장 작은 수 들 중에서 가장 큰 수 찾기
    result = max(result, min_value) # max(a,b) 두 인수 중 큰 수를 반환

  print(result)

def game_ex2():
  # N,M을 공백을 구분하여 입력받기
  N,M = map(int, input().split())
  
  result = 0
  for i in range(N):
    data = list(map(int, input().split()))

    min_value = 10001 # 조건 밖의 수
    for a in data:
      min_value = min(min_value, a) # min(a,b) 두 인수 중 작은 수를 반환
    result = max(result, min_value) # max(a,b) 두 인수 중 큰 수를 반환
  
  print(result)
