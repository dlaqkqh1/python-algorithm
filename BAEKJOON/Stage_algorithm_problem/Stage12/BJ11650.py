cnt = int(input())
arr = []

for x in range(cnt):
    arr.append(list(map(int, input().split())))

arr.sort()

for x in arr:
    print(x[0], x[1])
