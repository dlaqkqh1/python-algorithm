cnt = int(input())

for x in range(cnt):
    score = 0
    temp_score = 0
    
    case = input()
    for y in range(len(case)):
        if case[y] == 'O':
            score += temp_score + 1
            temp_score += 1
        else:
            temp_score = 0

    print(score)
