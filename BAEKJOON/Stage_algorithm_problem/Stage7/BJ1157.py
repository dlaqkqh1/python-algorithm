string = input()
string = string.upper()
arr = []
maxnum = -1
maxchar = ''

for x in range(26):
    arr.append(0)

for x in range(len(string)):
    arr[ord(string[x]) - 65] += 1

for x in range(26):
    if maxnum < arr[x]:
        maxnum = arr[x]
        maxchar = chr(x + 65)

    elif maxnum == arr[x]:
        maxchar = '?'

print(maxchar)
