#내 풀이
N = int(input())
score_dict = {}
score_list = []

for _ in range(N):
    name, score = input().split()
    score_dict[int(score)] = name
    score_list.append(int(score))

score_list = sorted(score_list)

for i in score_list:
    print(score_dict[i], end = ' ')
    

#교재 풀이
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))
  
array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')
