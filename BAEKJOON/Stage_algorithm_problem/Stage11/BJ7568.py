num = int(input())
arr = []
result = []

for x in range(num):
    temp = list(map(int, input().split()))
    arr.append(temp)
    result.append(1)

for x in range(len(arr)):
    for y in range(len(arr)):
        if x == y:
            continue
        if arr[x][0] < arr[y][0] and arr[x][1] < arr[y][1]:
            result[x] += 1

for x in result:
    print(x, end=' ')
