num = int(input())

a, b = (1, 1)

cnt = 0
for x in range(1, 10000000):
    if num > cnt:
        cnt += x
    else:
        a = 1 + cnt - num
        b = x - 1 - cnt + num
        break

if (a + b) % 2 == 1:
    print(str(b) + '/' + str(a))
else:
    print(str(a) + '/' + str(b))
