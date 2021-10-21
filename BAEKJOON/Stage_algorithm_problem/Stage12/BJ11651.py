cnt = int(input())
arr = []

for x in range(cnt):
    dot = list(map(int, input().split()))
    dot.reverse()
    arr.append(dot)

arr.sort()

for x in arr:
    print(x[1], x[0])
