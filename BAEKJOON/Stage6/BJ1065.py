def hansu(num):                                                    # 한수를 분별하는 함수
    arr = []

    while num != 0:                                                # 각자리의 숫자를 list로 저장
        arr.append(num % 10)
        num = int(num / 10)

    if len(arr) < 3:                                               # 1~99 까지는 무조건 한수로 취급
        return 1

    arr.reverse()                                                  # 일의 자리 숫자부터 들어감으로 역순으로 변경
    diff = arr[1] - arr[0]                                         # 첫번째 자리와 두번째 자리 숫자의 차이를 구함

    for x in range(1, len(arr) - 1):                               # 각 자리 숫자의 차이가 같은지 판별
        if arr[x + 1] - arr[x] == diff and x == len(arr) - 2:      # 차이가 모두 같은것으로 판명되면 han의 카운트 + 1
            return 1

        elif arr[x + 1] - arr[x] != diff:
            return 0

        else:
            continue


num = int(input())
han = 0                                                            # 한수 갯수를 담을 변수

for x in range(1, num + 1):
    han += hansu(x)


print(han)
