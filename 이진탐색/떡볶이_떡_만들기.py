"""
파라메트릭 서치 유형: 최적화 문제를 결정 문제로 바꿔 해결하는 방법(원하는 조건을 만족하는 가장 알맞는 값 찾기)
이진탐색으로 범위를 좁혀나가 해결하며 본 문제에서는 탐색범위인 절단기의 높이가 1부터 10억까지의 정수로 범위가 매우 넓으므로 이진 탐색을 쓰기 용이하다.

"""
N,M = map(int, input().split())
food = list(map(int, input().split()))

start = 0
end = max(food)
result = 0
while start < end:
    get = 0
    mid = (start+end) // 2
    for i in food:
        if i > mid:
            get += i - mid
    if get < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
