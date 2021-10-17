while True:
    
    circle_list = list(map(int, input().split()))

    c = max(circle_list)
    del(circle_list[circle_list.index(max(circle_list))])
    a, b = (circle_list[0], circle_list[1])
    if a == 0:
        break
    print('right' if c * c == a * a + b * b else 'wrong')
