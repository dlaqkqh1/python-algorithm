a = int(input())
b = int(input())
min_num = 100001
sum_num = 0
arr = [0, 0]


for x in range(10000):
    arr.append(1)

for x in range(2, 5001):
    if arr[x] == 0:
        continue
    for y in range(2, 5001):
        if x * y > 10000:
            break
        else:
            arr[x * y] = 0

for x in range(a, b + 1):
    if arr[x] == 1:
        sum_num += x
        if min_num > x:
            min_num = x

if sum_num == 0:
    print(-1)
else:
    print(sum_num)
    print(min_num)
