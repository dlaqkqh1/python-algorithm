a, b = map(int, input().split())

nums = list(map(int, input().split()))

for x in range(a):
    if nums[x] < b:
        print(nums[x], end = ' ')
