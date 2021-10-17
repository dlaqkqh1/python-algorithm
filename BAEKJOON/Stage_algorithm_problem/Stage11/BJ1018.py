m, n = map(int, input().split())
pan = []
diff = 100000


for x in range(n):
    line = input()
    pan.append(line)

print(pan)
for i in range(9 - m):
    for j in range(9 - n):
        cnt_black = 0
        cnt_white = 0
        for k in range(8):
            for l in range(8):
                if k % 2 == 0:
                    if l % 2 == 0 and pan[i + k] == 'B':
                        cnt_white += 1
                        continue
                    elif k % 2 == 1 and pan[i + k] == 'W':
                        cnt_black += 1
                        continue
                elif k % 2 == 1:
                    if l % 2 == 0 and pan[i + k] == 'W':
                        cnt_black += 1
                        continue
                    elif l % 2 == 1 and pan[i + k] == 'B':
                        cnt_white += 1
                        continue

        if cnt_black < diff:
            diff = cnt_black
        if cnt_white < diff:
            diff = cnt_black

print(diff)
