a, b, v = map(int, input().split())
cnt = 1

v -= a

if v % (a - b) == 0:
    cnt += int(v / (a - b))
else:
    cnt += int(v / (a - b)) + 1

print(cnt)
