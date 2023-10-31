M, N = map(int, input().split())

nums = {}

for i in range(1, N+1):
    nums[i] = i

for i in range(2, N+1):
    # 이미 지워진 숫자면 넘어가기
    if (nums[i] == 0):
        continue
    # i의 배수인 수들은 전부 없애기 (본인 제외: 본인은 소수이기때문)
    for j in range(i+i, N+1, i):
        if (j % i == 0):
            nums[j] = 0

for i in range(M, N+1):
    if (nums[i] != 0 and i != 1):
        print(i)