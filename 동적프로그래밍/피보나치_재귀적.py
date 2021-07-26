# memoization을 위해 리스트 초기화
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산했던 것은 리스트에서 불러오기
    if d[x] != 0:
        return d[x]
    # 처음 계산 하는 것은 리스트에 넣어주고 리턴
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
