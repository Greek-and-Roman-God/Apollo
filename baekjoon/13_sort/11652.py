# 11652 카드
# https://www.acmicpc.net/problem/11652
from collections import Counter
import sys


def input(): return sys.stdin.readline()


n = int(input())
num_list = [int(input()) for _ in range(n)]
count_list = Counter(num_list).most_common()
count_list.sort(key=lambda x: (-x[1], x[0]))
print(count_list[0][0])
