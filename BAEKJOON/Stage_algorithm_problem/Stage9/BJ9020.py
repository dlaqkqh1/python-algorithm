cnt = int(input())

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


for x in range(cnt):
    num = int(input())
    breaker = False
    for y in range(num // 2, 1, -1):
        if arr[y] == 0:
            continue
        for z in range(num // 2, num):
            if arr[z] == 0:
                continue
            if num == y + z:
                print(y, z)
                breaker = True
        if breaker == True:
            break
