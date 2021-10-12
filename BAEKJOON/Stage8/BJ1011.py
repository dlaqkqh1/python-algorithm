t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    num = y - x
    cnt = 0
    speed = 1
    tree = 0

    while True:
        if num < tree:
            speed -= 1
            num = num - (tree - (speed * 2) + 1)
            cnt += (speed - 2) * 2 + 1
            for j in range(1, speed):
                cnt += num // (speed - j)
                num %= (speed - j)
            break
        else:
            if speed < 2:
                tree = tree * 2 + speed
            else:
                tree = (((tree - (speed - 1)) // 2) + speed - 1) * 2 + speed
            speed += 1

    print(cnt)
