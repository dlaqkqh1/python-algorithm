def prime_number_generator(start, stop):
    for num in range(start, stop + 1):
        is_prime = True
        for n in range(2, int(num / 2)):
            if num % n == 0:
                is_prime = False
                break
        if is_prime:
            yield num


start, stop = map(int, input().split())
 
g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')