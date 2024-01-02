import sys
input = sys.stdin.readline

answers = []
while(True) :
  nums = list(map(int, input().split()))
  if nums == [0, 0, 0] : 
    break
  nums.sort()
  if ((nums[0]*nums[0]) + (nums[1]*nums[1]) == (nums[2]*nums[2])) :
    answers.append('right')
  else :
    answers.append('wrong')

for answer in answers :
  print(answer)
  