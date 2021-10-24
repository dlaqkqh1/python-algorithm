#include <iostream>
using namespace std;

int count = 0;
int n;

int promising(int i, int queens_list[])
{ 
    int k = 1;
    int chek = 1;
    while (k < i && chek)
    {
        if (queens_list[i] == queens_list[k] || abs(queens_list[i] - queens_list[k]) == (i - k))
            chek = 0;
        k += 1;
    }        
    return chek;
}

int back_tracking(int cnt, int queens_list[])
{
    //cout << n << endl;
    if (promising(cnt, queens_list))
        if (cnt == n)
        {
            count += 1;
        }
        else
        {
            for (int i = 1; i <= n; i++)
            {
                queens_list[cnt + 1] = i;
                back_tracking(cnt + 1, queens_list);
            }
        }
    return 0;
}

int main()
{
    cin >> n;
    
    int* queens_list = new int[n+1]();
    back_tracking(0, queens_list);
    cout << count;
    return 0;
}