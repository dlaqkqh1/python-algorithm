a = int(input())
cnt = 0

while 50000 <= a:
    a -= 50000
    cnt += 1

while 10000 <= a:
    a -= 10000
    cnt += 1
    
while 5000 <= a:
    a -= 5000
    cnt += 1
    
while 1000 <= a:
    a -= 1000
    cnt += 1
    
while 500 <= a:
    a-= 500
    cnt += 1
    
while 100 <= a:
    a -= 100
    cnt += 1
    
while 50 <= a:
    a -= 50
    cnt += 1
    
while 10 <= a:
    a -= 10
    cnt += 1
    
print(cnt)
