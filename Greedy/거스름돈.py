N = int(input())
count = 0

coin = [500, 100, 50, 10]

for i in coin:
    count += N // i
    N %= i
print(count)
