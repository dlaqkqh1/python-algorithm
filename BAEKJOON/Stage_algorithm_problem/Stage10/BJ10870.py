def fibonacci(num):
    if num < 2:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
num = int(input())
print(fibonacci(num))
