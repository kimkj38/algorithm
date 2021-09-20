import heapq
import sys

#초깃값
INF = int(1e9)

#도시의 개수, 통로의 개수, 메시지를 보낼 도시
n, m ,c = map(int, input().split())

#그래프 생성
graph = [[] for i in range(n+1)]

#최단거리 테이블
distance = [INF] * (n+1)

#x도시에서 y도시로의 비용(z)
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))
    
def dijkstra(c):
    q = []
    #시작 노드로 가는 비용은 0
    heapq.heappush(q, (0, c))
    distance[c] = 0
    
    while q:
        #최단 거리 노드
        dist, now = heapq.heappop(q)
        #이미 처리된 노드
        if distance[now] < dist:
            continue
        #현재 노드의 인접 노드
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
            
#알고리즘 수행
dijkstra(c)

#도달 가능한 노드의 개수
count = 0

#도달 가능 노드 중 가장 멀리 있는 노드와의 최단거리
max_distance = 0

for d in distance:
    #도달 할 수 있는 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)
        
print(count-1, max_distance)
