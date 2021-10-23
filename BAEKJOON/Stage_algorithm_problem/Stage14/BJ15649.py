import sys

def back_tracking(n_list, m_list):
    for i in n_list:
        if i not in m_list:
            m_list.append(i)
            if len(m_list) == m:
                for j in m_list:
                    print(j, end=' ')
                print()
            else:
                back_tracking(n_list, list(m_list))
            del(m_list[-1])


n_list = []
n, m = map(int, sys.stdin.readline().split())

for x in range(1, n + 1):
    n_list.append(x)

back_tracking(n_list, [])

