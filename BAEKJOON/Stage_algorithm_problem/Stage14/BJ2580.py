import sys

pan = []

for i in range(9):
    line = list(map(int, sys.stdin.readline().split()))
    pan.append(line)

print(pan)
