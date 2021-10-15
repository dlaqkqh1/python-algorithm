arr = []
string = input()

for x in range(26):
    arr.append(-1)

for x in range(len(string)):
    if arr[ord(string[x]) - 97] == -1:
        arr[ord(string[x]) - 97] = x

for x in range(26):
    print(arr[x], end=' ')
