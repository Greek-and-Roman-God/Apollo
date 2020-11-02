# Q1 모험가 길드
def ad_guild():
  number = int(input())
  ad_list = list(map(int, input().split(' ')))
  ad_list = sorted(ad_list)
  result = 0

  for num in range(0,len(ad_list)):
      number -= ad_list[num]
      num = num + ad_list[num] - 1

      if number <= 0: return result
      
      result += 1