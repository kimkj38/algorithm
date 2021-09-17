import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수
n, m = map(int, input().split())
#시작 노드 번호
start = int(input())
#노드 연결 그래프
graph = [[] for i in range(n+1)]
#최단거리 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선 정보 입력 받기
for _ in range(m):
    a,b,c = map(int, input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0, 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0
    
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        #이미 처리된 노드라면 무시
        if distance[now] < dist:
            continue
        #현재 노드와 연결된 다른 인접 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐, 다른 노드로 이동하는 거리가 더 짧을 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
            
#알고리즘 수행
dijkstra(start)
                    
#모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    #도달 할 수 없는 경우 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
