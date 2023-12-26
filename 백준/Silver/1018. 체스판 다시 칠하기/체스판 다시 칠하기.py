M, N = map(int, input().split()) # M: 세로수, N: 가로수
board = []
result = []

for _ in range(M): # M 만큼 반복을 실행한다.
  board.append(input())

"""
Q. a+b가 의미하는 건 무엇일까?
A. a+b가 짝수면, (0,0)으로부터 대각선방향 + 한칸씩 건너뛴 놈들
   a+b가 홀수면, (0,1)로부터 대각방향 + 한칸씩 건너뛴
"""

for i in range(M-7) : # (세로축) 8x8 블럭의 시작점을 나타내기 때문에 board index를 초과하기 않기 위해서 -7을 해준다.
    for j in range (N-7) : # (가로축) 위와 동일
        start_black = 0
        start_white = 0
        for a in range(i, i+8) : # i가 0일때 기준, 0~7
            for b in range(j, j+8) : # 위와 동일
                if (a + b) % 2 == 0 : # a+b가 짝수일 때
                    if board[a][b] != 'B' : 
                        start_white += 1
                    if board[a][b] != 'W' :
                        start_black += 1
                else : # i+j가 홀수일 때
                    if board[a][b] != 'W' :
                        start_white += 1
                    if board[a][b] != 'B' :
                        start_black += 1
                        
        result.append(start_black)
        result.append(start_white)
        
print(min(result))
            
            