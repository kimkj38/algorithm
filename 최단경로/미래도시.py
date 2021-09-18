#회사의 수, 경로의 개수
n, m = map(int, input().split())

#연결 리스트
connections = []
for i in range(m):
    a,b = map(int, input().split())
    connections.append((a,b))
    
#목적지, 소개팅
x, k = map(int, input().split())

#초기화값
INF = int(1e9)

#그래프 생성
graph = [[INF]*(n+1) for _ in range(n+1)]

#자기 자신에게 가는 비용은 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j] = 0
            
#점화식
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

#결과
distance = graph[1][k]+graph[k][x]

#도달할 수 없는 경우
if distance >= INF:
    print("-1")
#도달하는 경우
else:
    print(distance)
