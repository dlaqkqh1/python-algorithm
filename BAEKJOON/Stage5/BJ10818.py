import sys
a = int(input())

b = list(map(int, sys.stdin.readline().split()))

b.sort()

print(b[0], b[-1])
