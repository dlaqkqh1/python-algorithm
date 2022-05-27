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
    n = len(queens_list)
    if cnt == n - 1:
        count += 1
    else:
        for i in range(1, n):
            queens_list[cnt + 1] = i
            if promising(cnt + 1, queens_list):
                back_tracking(cnt + 1, list(queens_list))


queens_list = []
n = int(sys.stdin.readline())
count = 0

queens_list = [0] * (n + 1)

back_tracking(0, queens_list)
print(count)
