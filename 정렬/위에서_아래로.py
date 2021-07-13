N = int(input())
num_list = []

for _ in range(N):
    num_list.append(int(input()))
    
num_list = sorted(num_list, reverse=True)

for i in num_list:
    print(i, end=' ')
