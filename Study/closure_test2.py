def countdown(n):
    cnt = n + 1
    def down():
        nonlocal cnt
        cnt -= 1
        return cnt
    return down

n = int(input())
 
c = countdown(n)
for i in range(n):
    print(c(), end=' ')