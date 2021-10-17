def hanoi(num, a, b, c):
    global arr
    if num == 1:
        arr.append(a + ' ' + c)
    else:
        hanoi(num - 1, a, c, b)
        arr.append(a + ' ' + c)
        hanoi(num - 1, b, a, c)
    return arr


arr = []
num = int(input())
hanoi_arr = hanoi(num, '1', '2', '3')
print(len(hanoi_arr))
for x in hanoi_arr:
    print(x)
