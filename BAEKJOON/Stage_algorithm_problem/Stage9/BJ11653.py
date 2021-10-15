num = int(input())
arr = []
temp_num = num

for x in range(2, num + 1):
    arr.append(0)
    while True:
        if temp_num == 1:
            break
        elif temp_num % x != 0:
            break
        elif temp_num % x == 0:
            temp_num = temp_num // x
            arr[x - 2] += 1

    if temp_num == 1:
        break

if num == 1:
    num = 1
else:
    for x in range(len(arr)):
        for y in range(arr[x]):
            print(x + 2)
