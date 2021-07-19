def binary_search(array, target, start, end):
    temp = (start+end)//2
    if array[temp] == target:
        return temp
    
    elif array[temp] > target:
        return binary_search(array, target, start, temp-1)
    
    else:
        return binary_search(array, target, temp+1, end)
    
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
