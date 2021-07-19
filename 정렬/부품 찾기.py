N = int(input())
total = list(map(int, input().split()))
total.sort()
M = int(input())
search = list(map(int, input().split()))



def binary_search(array, target, start, end):
    if start > end:
        return None
    temp = (start+end)//2
    if array[temp] == target:
        return temp
    
    elif array[temp] > target:
        return binary_search(array, target, start, temp-1)
    
    else:
        return binary_search(array, target, temp+1, end)

for i in range(M):
    result = binary_search(total, search[i], 0, N-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

            
