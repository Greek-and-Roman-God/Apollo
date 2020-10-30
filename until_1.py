def until_1():
  n,k = map(int, input().split())
  result = 0
  
  while 1:
    if n % k == 0:
      n = n / k
      result += 1
    else:
      n = n - 1
      result += 1

    if n == 1: break


  print(result)

def until_1_ex1():
  n,k = map(int, input().split())
  result = 0

  # N이 K 이상이라면 K로 계속 나누기
  while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
      n -= 1
      result += 1
    # K로 나누기
    n //= k
    result += 1
  
  # 마지막으로 남은 수에 대해서 1씩 빼기
  while n > 1:
    n -= 1
    result += 1

def until_1_ex2():
  n,k = map(int, input().split())
  result = 0

  while True:
    target = (n // k) * k # k로 나누어 떨어지는 수로 만듦
    result += (n - target) # k로 나누고 남은 수를 1씩 빼는 횟수
    
    n = target # 중간값

    if n < k: break # n이 k로 나누어 질 수 없으므로 반복문 중단

    result += 1
    n //= k # 나누어진 몫을 n에 대입
  
  # 남은 수에 대해 1씩 뺌
  result += (n-1)
  print(result)