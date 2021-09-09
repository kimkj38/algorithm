# 다익스트라 알고리즘
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드, 간선의 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())
# 노드 연결에 대한 리스트
graph = [[] for i in range(n + 1)]
# 방문여부 체크 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n + 1)

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a노드에서 b노드로 가는 비용이 c
    graph[a].append((b, c))


# 방문하지 않은 노드 중 가장 최단 거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    # 노드에 연결된 노드 개수만큼 반복
    for j in graph[start]:
        # graph에서 비용에 대한 값 가져와 거리 리스트에 입력
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단거리가 가장 짧은 노드를 꺼내 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드들 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우
    if distance[i] == INF:
        print("INFINITY")
    # 도달 가능한 경우
    else:
        print(distance[i])
