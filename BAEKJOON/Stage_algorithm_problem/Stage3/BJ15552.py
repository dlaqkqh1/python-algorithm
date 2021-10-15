import sys
a = int(sys.stdin.readline())

for x in range(a):
    x, y = map(int, sys.stdin.readline().split())

    print(x + y)
