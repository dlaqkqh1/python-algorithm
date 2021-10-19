cnt = int(input())
arr = []

for x in range(cnt):
    arr.append(int(input()))

for x in range(cnt - 1):
    for y in range(cnt - x - 1):
        if arr[y] > arr[y + 1]:
            temp = arr[y]
            arr[y] = arr[y + 1]
            arr[y + 1] = temp

for x in arr:
    print(x)
