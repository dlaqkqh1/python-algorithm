def check(a):                                    # 그룹단어 판별 함수
    arr = []

    for x in range(26):
        arr.append(0)

    for x in range(len(a) - 1):                  # 앞뒤 문자가 다르면 체크 시작
        if a[x] != a[x + 1]:
            if arr[ord(a[x + 1]) - 97] != 0:     # 앞 문자가 이미 나온적 있으면 0을 반환
                return 0
            else:
                arr[ord(a[x]) - 97] = 1          # 앞뒤 문자가 달라지면 해당 문자 체크
        else:
            continue

    return 1


cnt = 0
num = int(input())

for x in range(num):
    string = input()
    cnt += check(string)

print(cnt)
