/*
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=3 ; task=1)
*/

#include <bits/stdc++.h>

#define endl '\n'

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    regex multiplication(R"(mul\((\d{1,3}),(\d{1,3})\))");
    int ans = 0;
    string line;
    while (getline(cin, line)) {
        smatch m;
        auto start = line.cbegin();
        while (regex_search(start, line.cend(), m, multiplication)) {
            ans += stoi(m[1].str()) * stoi(m[2].str());
            start = m.suffix().first;
        }
        cout << endl;
    }
    cout << ans << endl;
    return 0;
}
