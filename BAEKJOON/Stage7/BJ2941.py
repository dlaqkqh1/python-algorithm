def check1(a):    # 2글자 크로아티어 체크
    if 'c=' == a or 'c-' == a or 'd-' == a or 'lj' == a or 'nj' == a or 's=' == a or 'z=' == a:
        return 1


def check2(a):    # 3글자 크로아티어 체크
    if 'dz=' == a:
        return 1


string = input()
cnt = 0

while len(string) != 0:
    if len(string) >= 2 and check1(string[0:2]) == 1:   # 1번 케이스일 경우 두글자 제거 후 cnt + 1
        string = string[2:]
        cnt += 1

    elif len(string) >= 3 and check2(string[0:3]) == 1: # 3번 케이스일 경우 세글자 제거 후 cnt + 1
        string = string[3:]
        cnt += 1

    else:                                               # 이외의 케이스에서는 한글자 제거 후 cnt + 1
        string = string[1:]
        cnt += 1

print(cnt)
