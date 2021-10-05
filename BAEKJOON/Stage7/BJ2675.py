num = int(input())

for x in range(num):
    renum, string = input().split()
    result = ''

    for y in range(len(string)):
        for z in range(int(renum)):
            result += string[y]

    print(result)
