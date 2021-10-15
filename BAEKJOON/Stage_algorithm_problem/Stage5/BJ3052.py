arr = []
cnt = 0

for x in range(42):
    arr.append(0)

for x in range(10):
    a = int(input())
    arr[a % 42] += 1

for x in range(42):
    if arr[x] != 0:
        cnt += 1

print(cnt)
