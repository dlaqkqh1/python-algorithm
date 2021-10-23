import sys

def back_tracking(n_list, m_list):
    global m_list_list
    for i in n_list:
        if i not in m_list:
            m_list.append(i)
            if len(m_list) == m and set(m_list) not in (m_list_list):
                for j in m_list:
                    print(j, end=' ')
                print()
                m_list_list.append(set(m_list))
            else:
                back_tracking(n_list, list(m_list))
            del(m_list[-1])


m_list_list = []
n_list = []
n, m = map(int, sys.stdin.readline().split())

for x in range(1, n + 1):
    n_list.append(x)

back_tracking(n_list, [])