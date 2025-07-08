N, M, T = map(int, input().split())

round = [list(map(int, input().split())) for _ in range(N)]

for i in range(T):
    x, d, k = map(int, input().split())
    
    # x의 배수인 행
    max = N // x
    for m in range(max):
        # N행 중 x * m - 1 번째의 행
        temp_r = x * (m + 1) - 1
        
        # 시계(->) / 반시계(<-)
        if d == 0:
            round[temp_r] = round[temp_r][-k:] + round[temp_r][:-k]
        elif d == 1:
            round[temp_r] = round[temp_r][k:] + round[temp_r][:k]
            
    # 인접한 수 제거
    for r in range(N):
        for c in range(N):
            # 가로 비교
            # column의 0과 N - 1 비교
            if c == 0:
                if round[r][c] == round[r][N - 1]:
                    round[r][c], round[r][N - 1] = 0, 0
                elif c + 1 < N and round[r][c] == round[r][c + 1]:
                    round[r][c], round[r][c + 1] = 0, 0
            else:
                if 0 <= c - 1 and round[r][c] == round[r][c - 1]:
                    round[r][c], round[r][c - 1] = 0, 0
                elif c + 1 < N and round[r][c] == round[r][c + 1]:
                    round[r][c], round[r][c + 1] = 0, 0
                    
            # 세로 비교
            if 0 <= r - 1 and round[r][c] == round[r - 1][c]:
                round[r][c], round[r - 1][c] = 0, 0
            elif r + 1 < N and round[r][c] == round[r + 1][c]:
                round[r][c], round[r + 1][c] = 0, 0

result = 0
for i in range(N):
    result += sum(round[i])
    
print(result)

    
'''
문제이해:

* N, M, T:
N개의 원, 원 하나당 M개의 수, T번 회전
수는 서로 인접(가로, 세로)
인접한 수가 있는 경우, 인접한 수를 지운다
인접한 수가 없는 경우, 적힌 수의 평균보다 큰 수는 -1, 작은 수는 +1

* 1~N개의 원, 1~T번 회전
i: 1, 2, 3, ..., N
i: 1, 2, 3, ..., T

* xi, di, ki:
x의 배수인 원판을 d방향으로 k칸만큼 이동
d = 0 시계
d = 1 반시계

* 원판의 수:
1 이상, 1000 이하
인접한 수가 같은 경우 0으로 처리

ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
k=1, 시계 d = 0
1 1 2/ 3 -> 3/ 1 1 2 [-k:] + [:-k]

k = 3, 반시계 d = 1
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

'''