arr = [0, 0]

for x in range(246912):
    arr.append(1)

for x in range(2, 123457):
    if arr[x] == 0:
        continue
    for y in range(2, 123457):
        if x * y > 246912:
            break
        else:
            arr[x * y] = 0

while True:
    num = int(input())
    cnt = 0
    for x in range(num + 1, num * 2 + 1):
        if arr[x] == 1:
            cnt += 1

    if num == 0:
        break
    print(cnt)
