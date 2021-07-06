# 내 답안
N = int(input())
commands = list(input().split())
x,y = 1,1

for command in commands:
    if command == 'L':
        if y != 1:
            y -= 1
    elif command == 'R':
        if y != N:
            y += 1
    elif command == 'U':
        if x != 1:
            x -= 1
    elif command == 'D':
        if x != N:
            x += 1
   
print(x, y)
  
# 교재 답안
n = int(input())
x,y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L','R','U','D']

for plan in plans:
    for i range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x, y = nx, ny
    
print(x, y)
     
