/*
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=1 ; task=1)
*/

#include <bits/stdc++.h>

#define endl '\n'

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int a, b;
    vector<int> group1, group2;
    while (cin >> a >> b) {
        group1.push_back(a);
        group2.push_back(b);
    }
    sort(group1.begin(), group1.end());
    sort(group2.begin(), group2.end());
    int ans = 0;
    for (int i = 0; i < group1.size(); ++i) {
        ans += abs(group1[i] - group2[i]);
    }
    cout << ans << endl;
    return 0;
}
