a = int(input())

for z in range(1, a + 1):
    x, y = map(int, input().split())
    print('Case #' + str(z) + ': ' + str(x + y))
