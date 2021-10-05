a, b = input().split()
a_new, b_new = ('', '')

for x in range(3):
    a_new += a[2 - x]
    b_new += b[2 - x]

if a_new > b_new:
    print(a_new)
else:
    print(b_new)