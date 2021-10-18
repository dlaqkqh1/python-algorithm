num = int(input())
cnt = 1
temp_num = 666
breaker = False


while True:
    if cnt == num:
        break
    if str(temp_num + 1000).find('6666') != -1:
        temp = temp_num
        temp_str = str(temp_num + 1000)
        temp_cnt = 1

        while True:
            temp_str = temp_str[0:len(temp_str) - temp_cnt] + '0' * temp_cnt
            temp_num = int(temp_str)
            if str(temp_num).find('6666') == -1:
                break
            temp_cnt += 1
        cnt += 1
        for x in range(10 ** temp_cnt):
            if cnt == num:
                breaker = True
                break
            temp_num += 1
            cnt += 1
        if not breaker:
            temp_num = temp + 2000

    if breaker or cnt == num:
        break
    temp_num += 1000
    cnt += 1


print(temp_num)
