# http://www.codeup.kr/problem.php?id=2001

# 파스타와 주스 중 최소 금액을 각각 고르는 것이 해결법
pasta = 2001

for x in range(3): # 파스타의 최소금액 구하기
    a = int(input())
    if pasta > a:
        pasta = a
        
juice = 2001

for x in range(2): # 주스의 최소금액 구하기
    a = int(input())
    if juice > a:
        juice = a
        
total = (pasta + juice) * 1.1 # 10% 금액을 더하여 대금 계산

print(format(total, '.1f')) # format 함수를 통해 소수점 1자리 까지만 계산
