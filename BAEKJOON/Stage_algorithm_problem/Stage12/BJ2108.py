import sys
cnt = int(sys.stdin.readline())
arr = []
arr_cnt = [0] * 8001
num_sum = 0
is_first = 0
max_cnt = 0
is_mid = 0

for x in range(cnt):
    num = int(sys.stdin.readline())
    arr.append(num)
    arr_cnt[num + 4000] += 1

for y in range(8001):
    if arr_cnt[y] == 0:
        continue
    num_sum += arr_cnt[y]
    if num_sum > cnt // 2 and is_mid == 0:
        mod = y - 4000
        is_mid = 1
    if max(arr_cnt) == arr_cnt[y]:
        if is_first == 0:
            max_cnt = y - 4000
            is_first = 1
        elif is_first == 1:
            max_cnt = y - 4000
            is_first = 2


print(round(sum(arr) / cnt))
print(mod)
print(max_cnt)
print(max(arr) - min(arr))
