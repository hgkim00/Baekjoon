import sys
input=sys.stdin.readline

N, M = map(int, input().split())

def gcd(a, b) :
  while b > 0 :
    a, b = b, a % b
  return a

def lcm(a, b) :
  return int(a * b / gcd(a, b))

if (N > M) : 
  print(gcd(N, M))
  print(lcm(N, M))
else :
  print(gcd(M, N))
  print(lcm(M, N))