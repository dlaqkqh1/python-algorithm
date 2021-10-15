cnt = int(input())
arr = list(map(float, input().split()))
max_cnt = max(arr)

for x in range(cnt):
    arr[x] = arr[x] / max_cnt * 100

print(sum(arr) / len(arr))
