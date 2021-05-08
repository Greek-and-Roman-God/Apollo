# 국영수
import sys
input = sys.stdin.readline

n = int(input())

students = []
# lalal = [
#     ["Junkyu", "50", "60", "100"],
#     ["Sangkeun", "80", "60", "50"],
#     ["Sunyoung", "80", "70", "100"],
#     ["Soong", "50", "60", "90"],
#     ["Haebin", "50", "60", "100"],
#     ["Kangsoo", "60", "80", "100"],
#     ["Donghyuk", "80", "60", "100"],
#     ["Sei", "70", "70", "70"],
#     ["Wonseob", "70", "70", "90"],
#     ["Sanghyun", "70", "70", "80"],
#     ["nsj", "80", "80", "80"],
#     ["Taewhan", "50", "60", "90"],
# ]

for i in range(n):
    name, kor, eng, math = input().split()
    # name, kor, eng, math = lalal[i]

    students.append([-int(kor), int(eng), -int(math), name])

students.sort()

for _, _, _, name in students:
    print(name)
