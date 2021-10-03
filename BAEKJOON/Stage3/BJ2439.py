a = int(input())

for x in range(a):
    star = ''
    for y in range(a - x - 1):
        star += ' '
    for z in range(x + 1):
        star += '*'
    print(star)
