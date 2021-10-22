import sys

cnt = int(input())
temp = ''
arr = []
dict_count = dict()

arr = list(map(int, sys.stdin.readline().split()))

set_arr = set(arr)
temp_arr = list(set_arr)
temp_arr.sort()

for x in range(len(temp_arr)):
    dict_count[temp_arr[x]] = x

for x in arr:
    print(dict_count[x], end=' ')
