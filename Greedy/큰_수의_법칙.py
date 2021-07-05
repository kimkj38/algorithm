N, M, K = map(int, input().split())
num = list(map(int, input().split()))

first_num = max(num)
num.remove(first_num)
second_num = max(num)

SUM = 0
count = 0

while count < M:
    for j in range(K):
        SUM += first_num
        count += 1
    SUM += second_num
    count += 1

print(SUM)
