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
  
