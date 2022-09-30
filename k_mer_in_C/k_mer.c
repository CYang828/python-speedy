#include <iostream>
#include <string>
#include <time.h>

using namespace std;

char convert(char c)
{
    if (c == 'A')
        return 'C';
    if (c == 'C')
        return 'G';
    if (c == 'G')
        return 'T';
    if (c == 'T')
        return 'A';
    return ' ';
}

int main()
{
    cout << "开始" << endl;
    clock_t start, ends;
    start = clock();

    string opt = "ACGT";
    string s = "";
    string s_last = "";
    int len_str = 13;
    bool change_next;

    for (int i = 0; i < len_str; i++)
    {
        s += opt[0];
    }

    for (int i = 0; i < len_str; i++)
    {
        s_last += opt.back();
    }

    int pos = 0;
    int counter = 1;
    while (s != s_last)
    {
        counter++;
        // You can uncomment the next line to see all k-mers.
        // cout << s << endl;
        change_next = true;
        for (int i = 0; i < len_str; i++)
        {
            if (change_next)
            {
                if (s[i] == opt.back())
                {
                    s[i] = convert(s[i]);
                    change_next = true;
                }
                else
                {
                    s[i] = convert(s[i]);
                    break;
                }
            }
        }
    }

    // You can uncomment the next line to see all k-mers.
    // cout << s << endl;
    ends = clock();
    double cost = (double)(ends - start) / CLOCKS_PER_SEC;
    cout << "生成 k-mers 的数量: " << counter;
    cout << "\t花费时间: " << cost << " 秒" << endl;
    cout << "完成!" << endl;
    return 0;
}