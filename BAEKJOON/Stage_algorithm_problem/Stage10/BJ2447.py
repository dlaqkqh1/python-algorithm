def star_patterns(num):
    if num == 3:
        return ['***', '* *', '***']
    else:
        patterns = star_patterns(num // 3)
        new_patterns = []
        for x in range(3):
            if x == 0:
                for y in range(num // 3):
                    new_patterns.append(patterns[y] * 3)
            elif x == 1:
                for y in range(num // 3):
                    new_patterns.append(patterns[y] + ' ' * (num // 3) + patterns[y])
            else:
                for y in range(num // 3):
                    new_patterns.append(patterns[y] * 3)

    return new_patterns


num = int(input())
for x in star_patterns(num):
    print(x)


