# 수학
import math

N = int(input())
facN = math.factorial(N)

count = 0

while (facN % 10 == 0) :
  count += 1
  facN = facN // 10

print(count)