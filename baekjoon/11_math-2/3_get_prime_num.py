# 1929 소수 구하기
# https://www.acmicpc.net/problem/1929

m, n = map(int, input().split())

# 출력할 때 인덱스를 사용하기 위해 최대 인덱스가 n인 n+1길이의 리스트를 만들어줌
nums = [0] * (n+1)
# 0과 1은 소수가 아니기 때문에 미리 제외해준다.
nums[0] = nums[1] = -1
# print(nums)

# 소수를 판단하기 위해서 사용하는 숫자는
# 짝수를 판단하는 2부터 최대값인 n이 2에 나누어 떨어지는 수까지이기 때문에
# 2부터 n//2까지만 확인하면 소수를 판단할 수 있다.
for i in range(2, n//2+1):
    # 1배수는 소수인지 확인하지 않아도 되기 때문에 temp의 초기값은 2
    temp = 2
    while temp * i <= n:
        # 소수는 1와 나 자신으로만 나누어지는 수이기 때문에
        # i의 배수를 확인하면서 해당하는 수를 소수가 될 수 없으므로
        # 소수에서 제외시킨다.
        nums[temp * i] = -1
        temp += 1
        # print(f'i {i} temp {temp} num {num} <= {n}')

# print(nums)

for num in range(m, n + 1):
    # 원소가 0이 아닌 칸은 소수가 아님
    # 원소가 0(False)인 칸만 출력
    if not nums[num]:
        print(num)

# 에라토스테네스의체 제대로 읽어보고 다르게 풀어봄
# 뭐가 다른건지는 잘 모르겠다. 백준에서는 위의 코드보다 속도는 느리고 메모리가 적게 나옴
m, n = map(int, input().split())

nums = [0] * (n+1)
nums[0] = nums[1] = -1

for i in range(2, n//2+1):
    temp = 2
    if nums[i] == -1:
        continue
    while temp * i <= n:
        nums[temp * i] = -1
        temp += 1

for num in range(m, n + 1):
    if not nums[num]:
        print(num)
