string = input()
string = string.rstrip().lstrip()    # 앞, 뒤 공백 제거
cnt = 1

if string == '':                     # 공백만 입력 시 0개의 단어로 생각
    cnt = 0

for x in range(len(string)):
    if string[x] == ' ':
        cnt += 1

print(cnt)
