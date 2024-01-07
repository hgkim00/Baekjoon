import sys
input = sys.stdin.readline

N = int(input())
numCards = list(map(int, input().split()))

numDict = {}
for num in numCards :
  if (numDict.get(num) == None) :
    numDict[num] = 1
  else :
    numDict[num] += 1

M = int(input())
findNum = list(map(int, input().split()))
answer = []
for num in findNum :
  if (numDict.get(num) == None) :
    answer.append(0)
  else :
    answer.append(numDict[num])

for ans in answer :
  print(ans, end=" ")