pan = []

for x in range(10):
    a = input().split()
    pan.append(a)
    
x = 1
y = 1
while True:
    if (pan[x + 1][y] == '1' and pan[x][y + 1] == '1') or pan[x][y] == '2':
        pan[x][y] = '9'
        break
    pan[x][y] = '9'
    
    if pan[x][y + 1] == '0':
        y += 1
    else:
        x += 1
    
for i in range(10):
    for j in range(10):
         print(pan[i][j], end = ' ')
    print()
