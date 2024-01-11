import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

result = 0
# 이렇게 하면 리스트 내에서 3가지 수를 선택하는 모든 경우의 수를 파악할 수 있음
for i in range(N) :
  for j in range(i+1, N) :
    for k in range(j+1, N) :
      sum = nums[i] + nums[j] + nums[k]
      if (sum > M) :
        continue
      else :
        result = max(result, sum)

print(result)