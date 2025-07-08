N, M, T = map(int, input().split())

round = [list(map(int, input().split())) for _ in range(N)]

for i in range(T):
    x, d, k = map(int, input().split())
    
    # x의 배수인 행
    max = N // x
    for m in range(1, max + 1):
        # N행 중 x * m - 1 번째의 행
        temp_r = x * m - 1
        
        # 시계(->) / 반시계(<-)
        if d == 0:
            round[temp_r] = round[temp_r][-k:] + round[temp_r][:-k]
        elif d == 1:
            round[temp_r] = round[temp_r][k:] + round[temp_r][:k]
            
    ri = [-1, 1, 0, 0]
    ci = [0, 0, -1, 1]
    
    # 인접한 수 있는지 확인
    adj = False
    
    # 인접한 수 제거
    for r in range(N):
        for c in range(M):
            
            # 먼저 3개 비교
            # 범위내 가로
            if c + 2 < M and round[r][c] == round[r][c + 1] == round[r][c + 2] and round[r][c] != 0:
                round[r][c], round[r][c + 1], round[r][c + 2] = 0, 0, 0
            # 범위내 세로
            # if r + 2 < N and round[r][c] == round[r + 1][c] == round[r + 2][c] and round[r][c] != 0:
            #     round[r][c], round[r + 1][c], round[r + 2][c] = 0, 0, 0
            # -1, 0, 1 or -2, -1, 0인 경우
            if c == 0 and round[r][0] == round[r][-1] == round[r][-2] and round[r][0] != 0:
                round[r][0], round[r][-1], round[r][-2] = 0, 0, 0
            elif c == 0 and round[r][0] == round[r][-1] == round[r][1] and round[r][0] != 0:
                round[r][0], round[r][-1], round[r][1] = 0, 0, 0
        	
            # 다음으로 2개 비교
            # 범위내 가로세로 비교
            for i in range(4):
                dr, dc = r + ri[i], c + ci[i]
             
                if 0 <= dr < N and 0 <= dc < M and round[r][c] != 0:
                    if round[r][c] == round[dr][dc]:
                        round[r][c], round[dr][dc] = 0, 0
                        
                        # 인접한 수 있는지 확인
                        if adj == False:
                            adj = True
        	
        	# 가로 맨앞 & 맨끝 비교
            if c == 0 and round[r][c] == round[r][M - 1] and round[r][c] != 0:
                round[r][c], round[r][M - 1] = 0, 0
                
                # 인접한 수 있는지 확인
                if adj == False:
                    adj = True
    
    # 인접한 수가 없었다면
    if adj == False:
        result = 0 
        not_zero = 0
        
        for r in range(N):
            if sum(round[r]) != 0:
                result += sum(round[r])
                
                for c in range(M):
                    if round[r][c] != 0:
                        not_zero += 1
                        
        avg = result / not_zero
        
        # 평균보다 작으면 +1, 크면 -1
        for r in range(N):
            for c in range(M):
                if round[r][c] != 0:
                    if round[r][c] < avg:
                        round[r][c] += 1
                    elif round[r][c] > avg:
                        round[r][c] -= 1
            
result = 0
for i in range(N):
    result += sum(round[i])
     
print(result)

# 만약 세 인접한 수가 같으면? 먼저 0으로 처리해줘야 함
    
'''
문제이해:

* N, M, T:
N개의 원, 원 하나당 M개의 숫자, T번 회전
즉, 배열의 가로, 세로, 쿼리의 개수

수는 서로 인접(가로, 세로)
인접한 수가 있는 경우, 인접한 수를 지운다
인접한 수가 없는 경우, 적힌 수의 평균보다 큰 수는 -1, 작은 수는 +1

* xi, di, ki:
x의 배수인 원판을 d방향으로 k칸만큼 이동

xi의 배수인 행에서 숫자가 가로로 이동
d = 0 시계: 오른쪽 이동, [-k:] + [:-k]
d = 1 반시계: 왼쪽 이동, [k:] + [:k]

* 원판의 수:
1 이상, 1000 이하
인접한 수가 같은 경우 0으로 처리

* 1~N개의 원, 1~T번 회전
i: 1, 2, 3, ..., N
i: 1, 2, 3, ..., T

ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
k=1, 시계 d = 0, 오른쪽
1 1 2/ 3 -> 3/ 1 1 2 [-k:] + [:-k]

k = 3, 반시계 d = 1, 왼쪽
5 2 4/ 2 -> 2/ 5 2 4 [k:] + [:k]
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

반시계 방향으로 작은 원부터 작성
1 1 2 3
5 2 4 2
3 1 3 5

3 1 1 2 시계방향 (-> 1)
5 2 4 2
3 1 3 5

1 1 2 3
2 5 2 4 반시계방향 (<- 3)
5 3 1 3 반시계방향 (<- 3)

2 3 1 1 시계방향 (-> 2)
5 2 4 2
3 5 3 1 시계방향 (-> 2)
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

1 2 3 4 5 6
2 3 4 5 6 7
3 4 5 6 7 8
4 5 6 7 8 9

쿼리 1:
2 1 4 왼쪽
1 2 3 4 5 6
6 7 2 3 4 5
3 4 5 6 7 8
8 9 4 5 6 7

인접한 수 없음, 평균 = 5
2 3 4 5 5 5
5 6 3 4 5 5
4 5 5 5 6 7
7 8 5 5 5 6 -> 모든 줄에서 5가 3개

쿼리 2:
3 0 1 오른쪽
2 3 4 0 0 0
0 6 3 4 0 0
0 4 0 0 0 0
0 8 0 0 0 0

쿼리 3:
2 1 2 왼쪽
2 3 4 0 0 0
3 0 0 0 0 6
0 0 0 0 0 0
0 0 0 0 0 8
합: 26

'''