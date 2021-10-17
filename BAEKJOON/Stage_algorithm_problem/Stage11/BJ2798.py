n, m = map(int, input().split())
cards = list(map(int, input().split()))
diff = 10000000

for x in range(n):
    for y in range(n):
        if y == x:
            continue
        for z in range(n):
            if z in (x, y):
                continue
            if cards[x] + cards[y] + cards[z] <= m and m - cards[x] - cards[y] - cards[z] < diff:
                cards_sum = cards[x] + cards[y] + cards[z]
                diff = m - cards[x] - cards[y] - cards[z]

print(cards_sum)
