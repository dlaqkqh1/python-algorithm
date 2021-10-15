cnt = int(input())

for x in range(cnt):
    h, w, n = map(int, input().split())
    x, y = (1, 1)
    n -= 1
    x += n % h
    y += int(n / h)

    print(x * 100 + y)
