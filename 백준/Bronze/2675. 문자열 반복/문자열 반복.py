import sys
input = sys.stdin.readline

N = int(input())

answer = []
for _ in range(N):
  repeat, string = map(str, input().split())
  repeat = int(repeat)
  result = ''
  for s in string :
    result += s*repeat
  answer.append(result)

for i in answer :
  print(i)