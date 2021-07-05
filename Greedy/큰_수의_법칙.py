N, M, K = map(int, input().split())
num = list(map(int, input().split()))

first_num = max(num)
num.remove(first_num)
second_num = max(num)

count = M // (K+1) * K #가장 큰 수가 더해지는 횟수
count += M % (K+1)

SUM = 0
SUM += count * first_num
SUM += (M-count) * second_num

print(SUM)
