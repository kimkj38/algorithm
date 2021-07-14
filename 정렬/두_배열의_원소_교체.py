#내 풀이
import numpy as np

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(k):
    min_a = np.argmin(A)
    max_b = np.argmax(B)
    A[min_a], B[max_b] = B[max_b], A[min_a]
print(sum(A))

#교재 풀이(numpy를 사용 안하며, 정렬에 더 적합)
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
    
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))


