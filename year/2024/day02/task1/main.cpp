/*
Author : Jose A.Romero
Puzzle : Advent of Code(year=2024 ; day=2 ; task=1)
*/

#include <bits/stdc++.h>

#define endl '\n'

using namespace std;

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    string line;
    int ans = 0;
    while (getline(cin, line)) {
        istringstream s(line);
        vector<int> nums;
        bool cond1 = true, cond2 = true;
        int last, cur;
        s >> last;
        while (s >> cur) {
            cond1 &= 1 <= cur - last && cur - last <= 3;
            cond2 &= -3 <= cur - last && cur - last <= -1;
            last = cur;
        }
        ans += cond1 || cond2;
    }
    cout << ans << endl;
    return 0;
}
