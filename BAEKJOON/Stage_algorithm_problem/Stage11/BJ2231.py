num = int(input())
result = 0

for x in range(1, num):
    temp = x
    temp_sum = x
    while temp > 0:
        temp_sum += temp % 10
        temp //= 10
    if temp_sum == num:
        result = x
        break
print(result)
