# http://www.codeup.kr/problem.php?id=3301

# 남은 온도를 아래서 올릴지 위에서 내릴지 결정하는 것이 중요

a, b = input().split()
a = int(a)
b = int(b)

if a == b:                 # 만약 현재 온도와 목표 온도가 같다면 즉시 종료
    print(0)
    exit()

num = abs(b-a)             # 목표 온도까지 얼마의 온도가 필요한지 절대값으로 정의
cnt = 0                    # 올린 횟수를 저장할 변수 선언

while True:
    if num >= 10:          # 10보다 작을 때 까지 축소
        num -= 10
    elif num >= 8:         # 8이상이면 10도를 올려서 빼는게 더 빠르므로 10 - num
        num = 10 - num
    elif num >= 5:         # 5 미만으로 축소
        num -= 5
    elif num >= 3:         # 3이상이면 5도를 올려서 빼는게 더 빠르므로 10 - num
        num = 5 - num
    else:
        num -= 1           # 2미만 부터는 그냥 1씩 올리거나 내림
    cnt += 1               # 카운트 증가

    if num <= 0:           # 목표온도에 도달하면 while문 탈출
        break

print(cnt)
