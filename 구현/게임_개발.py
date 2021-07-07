#행, 열의 개수
N, M = map(int, input().split())

#현재 위치 및 바라보는 방향
A, B, D = map(int, input().split())

#area 만들어주기
area = []
for i in range(N):
    area.append(list(map(int, input().split())))

#현재 위치 좌표
loc = [A, B]

count = 0 # 움직일때마다 증가
check = 0 # 방향 전환 했는데 못 움직일 경우 증가

#방향에 따른 이동
steps = {0:(-1, 0), 1:(0, 1), 2:(1,0), 3:(0,-1)}

#바라보는 방향 순서(반시계 방향)
D_rotation = [0, 3, 2, 1, 0, 3] #북, 서, 남, 동


#4면이 전부 가본 곳이거나 바다면 종료
while check < 4:
    #현재 위치 2(가본 곳)로 지정
    area[loc[0]][loc[1]] = 2

    #바라보는 방향 변경
    for i, d in enumerate(D_rotation):
        if D == d:
            D = D_rotation[i+1]
            break
            

    # temp에 loc 복사 후 이동
    temp = loc.copy()
    temp[0] += steps[D][0]     
    temp[1] += steps[D][1]

    #이동 결과 공간을 벗어나지 않고, 바다가 가본 곳이 아닌 경우에만 loc를 바꿔준다
    if 0 <= temp[0] < N and 0 <= temp[1] < M:
        if area[temp[0]][temp[1]] == 0:
            loc = temp
            count += 1
            check = 0 #움직이면 check는 초기화
        else:
            check += 1
    else:
        check += 1
        
         
# 네 방향 모두 못 가는 경우 뒤로 이동
for i, d in enumerate(D_rotation):
    if D == d:
        move = D_rotation[i + 2]
        break
        
while True:
    loc[0] += steps[move][0]
    loc[1] += steps[move][1]
    
    #뒤가 바다인 경우 종료
    if area[loc[0]][loc[1]] == 1:
        break
    else:
        count += 1
