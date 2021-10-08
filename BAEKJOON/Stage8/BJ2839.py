num = int(input())

cnt = -1
five = num // 5

for x in range(five + 1):
    if (num - five * 5) % 3 == 0:
        num -= five * 5
        cnt = num // 3 + five
        break
    else:
        five -= 1

print(cnt)
