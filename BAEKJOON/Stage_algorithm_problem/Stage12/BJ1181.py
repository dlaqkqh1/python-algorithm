import sys

temp = ''
arr = []

for x in range(int(input())):
    arr.append(sys.stdin.readline().strip())

arr.sort(key=lambda x: (len(x), x))

for x in arr:
    if temp == x:
        continue
    else:
        print(x)
    temp = x
