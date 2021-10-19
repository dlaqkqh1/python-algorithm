import sys

cnt = int(sys.stdin.readline())
arr = [0] * 10001

for x in range(cnt):
    arr[int(sys.stdin.readline())] += 1

for x in range(10001):
    if arr[x] != 0:
        for y in range(arr[x]):
            print(x)