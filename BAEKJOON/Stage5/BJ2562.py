arr = []
maxindex = 0
maxnum = -1
for x in range(9):
    num = int(input())
    arr.append(num)

for x in range(9):
    if maxnum < arr[x]:
        maxnum = arr[x]
        maxindex = x + 1

print(str(maxnum) + '\n' + str(maxindex))