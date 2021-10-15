a = int(input())
b = int(input())
c = int(input())
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
num = a * b * c

while True:
    arr[num % 10] += 1
    num = int(num / 10)

    if num == 0:
        break

for x in range(10):
    print(arr[x])
