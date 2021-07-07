#내 풀이
cmd = input()
row = int(cmd[1])
col = cmd[0]

row_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
change_list = []
count = 8

for i, alpha in enumerate(row_list, 1):
    if row == alpha:
        row = i

change_list.append([col+2, row+1])
change_list.append([col+2, row-1])
change_list.append([col-2, row-1])
change_list.append([col-2, row-1])
change_list.append([col+1, row+2])
change_list.append([col+1, row-2])
change_list.append([col-1, row+2])
change_list.append([col-1, row-2])

for coor in change_list:
    if coor[0] < 1 or coor[0] > 8 or coor[1] < 1 or coor[1] > 8:
        count -= 1

print(count)

#교재 풀이
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 #반복문 없이 알파벳을 숫자로 바꿔줄 수 있다.

#유사 문제에서 공식처럼 사용한다고 생각해야겠다.
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1
 
print(result)

