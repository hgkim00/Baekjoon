T = int(input())

pattern = {0:0}

init = -1
for i in range(1, 10) :
  for j in range(1, 11) :
    if (j == 1) :
      init = i
    else :
      num = i ** j
      # print("init: " + str(init) + ", num: " + str(num))
      if (init == (num % 10)):
        # print("겹치는 패턴: " + str(j-1))
        pattern.update({init : j-1})
        break

answers = []
# 4 16 64 256 4
for i in range(T) :
  a, b = map(int, input().split())
  dupl = pattern[a % 10]
  if (dupl == 0) :
    answers.append(10)
    continue
  if (dupl == 1) :
    b = 1
  elif (dupl == 2) :
    b = b % 2
    if (b == 0) :
      b = 2
  elif (dupl == 4) :
    b = b % 4
    if (b == 0) :
      b = 4
  answers.append(a ** b % 10)

for i in answers:
  print(i)