import sys


def promising(i, queens_list):
    k = 1
    chek = True
    while k < i and chek:
        if queens_list[i] == queens_list[k] or abs(queens_list[i] - queens_list[k]) == (i - k):
            chek = False
        k += 1

    return chek


def back_tracking(cnt, queens_list):
    global count
    n = len(queens_list) - 1
    if promising(cnt, queens_list):
        if cnt == n:
            count += 1
        else:
            for i in range(1, n + 1):
                queens_list[cnt + 1] = i
                back_tracking(cnt + 1, queens_list)


queens_list = []
n = int(sys.stdin.readline())
count = 0

queens_list = [0] * (n + 1)

back_tracking(0, queens_list)
print(count)
