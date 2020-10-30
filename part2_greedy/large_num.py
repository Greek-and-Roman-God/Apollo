def large_num():
  n,m,k = map(int,input().split())
  data = list(map(int,input().split()))
  data.sort()

  first = data[len(data)-1]
  second = data[len(data)-2]

  result = 0
  count = 0
  chk_cnt = 1

  while not (count == m):

    if chk_cnt % k != 0:
      result = result + first
      chk_cnt = chk_cnt + 1
      count = count + 1
    else:
      result = result + second
      chk_cnt = 1
      count = count + 1
    
  
  print(result)

def ex_large_num():
  n,m,k = map(int,input().split())
  data = list(map(int,input().split()))
  data.sort()

  first = data[len(data)-1]
  second = data[len(data)-2]

  # 가장 큰 수가 반복된 횟수
  count = int(m / (k + 1)) * k + m % (k + 1)

  # 왜 result는 초기값을 선언해주는데 count는 안해주지
  # result = 0
  result = first * count + second * (m - count)

  print(result)
 