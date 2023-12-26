"""
사용한 알고리즘
- 정렬
- 이분 탐색 (binary search)
"""

N = int(input()) # A Length
A = list(map(int, input().split()))
A.sort()

M = int(input()) # Nums Length
Nums = list(map(int, input().split()))

isExist = False

for num in Nums :
  start = 0 			# 맨 처음 위치
  end = N-1 	# 맨 마지막 위치

  while start <= end:
      mid = (start + end) // 2 # 중간값

      if A[mid] == num :
          isExist = True
          print(1) 		# target 위치 반환
          break
      elif A[mid] > num: # target이 작으면 왼쪽을 더 탐색
          end = mid - 1
      else:                    # target이 크면 오른쪽을 더 탐색
          start = mid + 1
  if (isExist == False) :
    print(0) 
  isExist = False