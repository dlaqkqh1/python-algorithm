num = int(input())
arr = list(map(int, input().split()))
cnt = 0

for x in range(num):
    for y in range(2, arr[x] // 2 + 2):
        if arr[x] // 2 + 1 == y:
            cnt += 1
            break
        elif arr[x] % y != 0:
            continue
        else:
            break

print(cnt)
