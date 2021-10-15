a, b, c = map(int, input().split())
cnt = 0

if b >= c:
    cnt = -1

else:
    cnt = a / (c - b) + 1

print(int(cnt))
