/*
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=3 ; task=2)
*/

#include <bits/stdc++.h>

#define endl '\n'

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    regex multiplication(R"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))");
    int ans = 0;
    bool enabled = true;
    string line;
    while (getline(cin, line)) {
        smatch m;
        auto start = line.cbegin();
        while (regex_search(start, line.cend(), m, multiplication)) {
            if (m[0].str() == "do()") {
                enabled = true;
            }
            else if (m[0].str() == "don't()") {
                enabled = false;
            }
            else if (enabled) {
                ans += stoi(m[1].str()) * stoi(m[2].str());
            }
            start = m.suffix().first;
        }
        cout << endl;
    }
    cout << ans << endl;
    return 0;
}
