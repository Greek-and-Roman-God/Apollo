# 15596 정수 N개의 합
# https://www.acmicpc.net/problem/15596

# 통과
def solve1(a: int) -> int:
    return sum(a)


# 통과
def solve2(a: int) -> int:

    result = 0

    for num in a:
        result += num

    return result
