# 1924 2007년
# https://www.acmicpc.net/problem/1924
x, y = map(int, input().split())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = (sum(days[:x-1]) + y) % 7
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
print(week[day])
