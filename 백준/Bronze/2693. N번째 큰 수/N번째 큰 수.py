import sys
input = sys.stdin.readline

N = int(input())

answer = []
for _ in range(N) :
  nums = input().split()
  nums = list(map(int, nums))
  nums.sort(reverse=True)
  answer.append(nums[2])

for i in answer :
  print(i)