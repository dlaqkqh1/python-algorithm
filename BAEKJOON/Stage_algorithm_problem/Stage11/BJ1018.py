m, n = map(int, input().split())
pan = []
diff = 100000


for x in range(m):
    line = input()
    pan.append(line)

for i in range(m - 7):
    for j in range(n - 7):
        cnt_black = 0
        cnt_white = 0
        for k in range(8):
            for l in range(8):
                if k % 2 == 0:
                    if l % 2 == 0 and pan[i + k][j + l] == 'B':
                        cnt_white += 1
                    elif l % 2 == 0 and pan[i + k][j + l] == 'W':
                        cnt_black += 1
                    elif l % 2 == 1 and pan[i + k][j + l] == 'B':
                        cnt_black += 1
                    elif l % 2 == 1 and pan[i + k][j + l] == 'W':
                        cnt_white += 1
                elif k % 2 == 1:
                    if l % 2 == 0 and pan[i + k][j + l] == 'W':
                        cnt_white += 1
                    elif l % 2 == 0 and pan[i + k][j + l] == 'B':
                        cnt_black += 1
                    elif l % 2 == 1 and pan[i + k][j + l] == 'W':
                        cnt_black += 1
                    elif l % 2 == 1 and pan[i + k][j + l] == 'B':
                        cnt_white += 1

        if cnt_black < diff:
            diff = cnt_black
        if cnt_white < diff:
            diff = cnt_white

print(diff)

