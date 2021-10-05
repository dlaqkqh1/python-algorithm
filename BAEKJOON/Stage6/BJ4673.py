arr = []


def self_num(num):             # self_num 이 아닌 값을 찾는 함수
    result = num

    while num != 0:            # 각 자릿수를 더하는 반복문
        result += num % 10
        num = int(num / 10)

    return result


for x in range(10100):         # List의 index 길이 초과 방지를 위해 넉넉하게 생성
    arr.append(0)

for x in range(10000):         # self_num 이 아닌값을 1로 설정
    arr[self_num(x)] = 1

for x in range(10000):
    if arr[x] == 0:
        print(x)
