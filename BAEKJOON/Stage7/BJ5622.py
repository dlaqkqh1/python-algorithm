num = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
string = input()
result = 0

for x in range(len(string)):
    result += num[ord(string[x]) - 65]

print(result)
