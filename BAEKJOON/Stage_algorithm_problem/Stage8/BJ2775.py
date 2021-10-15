num = int(input())

for x in range(num):
    k = int(input())
    n = int(input())

    arr = []

    for i in range(k + 1):
        temparr = [0]
        cnt = 0
        for j in range(1, n + 1):
            if i == 0:
                temparr.append(j)
            else:
                cnt += arr[i - 1][j]
                temparr.append(cnt)

        arr.append(temparr)

    print(arr[k][n])
