a = int(input())
cycle = a
cnt = 0
while True:
    cycle = ((cycle % 10) * 10) + ((int(cycle / 10) + (cycle % 10)) % 10)
    cnt += 1
    if cycle == a:
        break

print(cnt)
