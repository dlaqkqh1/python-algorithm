cnt = int(input())

for x in range(cnt):
    over_cnt = 0
    
    arr = list(map(int, input().split()))
    length = arr[0]
    del(arr[0])
    
    avg = sum(arr) / len(arr)
    
    for y in range(length):  
        if arr[y] > avg:
            over_cnt += 1
    
    print('{:.3f}%'.format(round(over_cnt / len(arr) * 100, 3)))
