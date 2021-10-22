import sys

cnt = int(input())
arr = []

for x in range(cnt):
    age, name = sys.stdin.readline().split()
    arr.append([int(age), name])

arr.sort(key=lambda x:x[0])

for x in arr:
    print(x[0], x[1])
