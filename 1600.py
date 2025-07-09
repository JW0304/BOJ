import sys
input = sys.stdin.readline

import heapq

K = int(input())
W, H = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(H)]

prefix = [[0] * W for _ in range(H)]

hrow = [-2, -1, 1, 2]
hcol = [1, 2, 2, 1]
 
# 비지 않았으면 하나하나 빼서 출발점으로 지정
temp = []
next = []
r, c = 0

# K만큼 나이트 이동(0, 1, 2, ..., K)
for ki in range(K):

    while len(temp) != 0:
        r, c = heapq.heappop(temp)
        
        for i in range(4):
            hr = r + hrow[i]
            hc_l = c - hcol[i]
            hc_r = c + hcol[i]
                
            # 나이트 이동: 왼쪽, 오른쪽
            if 0 <= hr < H and 0 <= hc_l < W:
                if mat[hr][hc_l] == 0:
                    prefix[hr][hc_l] += 1
                    next.append((hr, hc_l))
            
            if 0 <= hr < H and 0 <= hc_r < W:
                if mat[hr][hc_r] == 0:
                    prefix[hr][hc_r] += 1
                    next.append((hr, hc_r))
            
            # 다음에 갈 수 있는 곳이 없으면 -1 출력하고 끝
            if next != []:
                break
            else:
                temp = next
                
            # 델타 이동
            for r in range(H):
                for c in range(W):
                    if 
        
# 나머지는 델타 이동, 델타 이동한 값이 더 작을때만 갱신
# 해당값 = 왼쪽값 + 위쪽값 - 왼쪽위값
for mat[hr][hc_l] + mat[hr][hc_r] -mat[j][]
    

'''
문제 풀이:
원숭이 r, c일 때

말(K번): 윗줄에서부터
(r-2, c-1), (r-2, c+1)
(r-1, c-2), (r-1, c+2)
(r+1, c-2), (r+1, c+2)
(r+2, c-1), (r+2, c+1)
원숭이(K번 이후): 델타로 이동

매트릭스:
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0

최소이동:
0 1 2 3
-1 2 1 2
0 1 -1 3
0 -1 0 4
'''


'''
문제 정보:
0, 0 에서 H - 1, W - 1까지 이동

최소 이동 횟수를 매트릭스에 작성한다
K번 나이트 이동하고 나머지는 델타 이동

0은 평지, 1은 장애물
시작점, 도착점은 평지(0)

도착 불가능한 경우 result = -1
'''