'''
사용 알고리즘
- Queue
가로로 눕혀놓은 스택이라고 생각하자 (일종의 파이프)
'''

import sys, queue
input = sys.stdin.readline

myQueue = queue.Queue()
N = int(input())

answer = []
for _ in range(N) :
  cmd = input().split()
  if (cmd[0] == 'push') :
    myQueue.put(int(cmd[1]))
  elif (cmd[0] == 'pop') :
    if (myQueue.empty()) :
      answer.append(-1)
    else :
      answer.append(myQueue.get())
  elif (cmd[0] == 'size') :
    answer.append(myQueue.qsize())
  elif (cmd[0] == 'empty') :
    if (myQueue.empty()) :
      answer.append(1)
    else :
      answer.append(0)
  elif (cmd[0] == 'front') :
    if (myQueue.empty()) :
      answer.append(-1)
    else :
      answer.append(myQueue.queue[0])
  elif (cmd[0] == 'back') :
    if (myQueue.empty()) :
      answer.append(-1)
    else :
      answer.append(myQueue.queue[-1])

for i in answer :
  print(i)