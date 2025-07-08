# 브루트 포스, 시간 초과

N, M = map(int, input().split())

matrix = []
row = []

for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
    
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    total = 0
    
    r1, c1, r2, c2 = x1-1, y1-1, x2-1, y2-1
    
    for r in range(N):
        for c in range(N):
            if r1 <= r <= r2 and c1 <= c <= c2:
                    total += matrix[r][c]
                
    print(total)
    
'''
행, 열 r, c
row 초기화
matrix는 2차원

(x1, y1), (x2, y2)
x1부터 x2
y1부터 y2

for문에서 범위 지정
x1 <= x <= x2
y1 <= y <= y2
'''